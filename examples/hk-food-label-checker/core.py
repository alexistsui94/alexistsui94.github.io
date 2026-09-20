# confidentiality: public-approved
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from typing import List, Optional

import dashscope
from dashscope import MultiModalConversation


MODEL_NAME = os.getenv("QWEN_VL_MODEL", "qwen-vl-max")


@dataclass
class ExtractionResult:
    success: bool
    ingredients: List[str] = field(default_factory=list)
    raw_text: str = ""
    error: str = ""


@dataclass
class TextOnlyResult:
    success: bool
    raw_text: str = ""
    error: str = ""


@dataclass
class LayoutBlock:
    role: str = "paragraph"
    label_original: str = ""
    label_hk: str = ""
    value_original: str = ""
    value_hk: str = ""
    original_text: str = ""
    hk_text: str = ""


@dataclass
class LayoutResult:
    success: bool
    blocks: List[LayoutBlock] = field(default_factory=list)
    raw_text: str = ""
    error: str = ""


class IngredientExtractor:
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("DASHSCOPE_API_KEY", "").strip()
        self.model = model or os.getenv("QWEN_VL_MODEL", "qwen-vl-max")
        if self.api_key:
            dashscope.api_key = self.api_key

    @staticmethod
    def _ingredient_prompt() -> str:
        return (
            "你是一个专业的食品标签识别助手。请只提取图片中的“配料表/成分表”内容，"
            "忽略品牌、广告语、营养成分表、食用方法、企业信息。\n"
            "请按以下要求输出：\n"
            "1. 将配料拆分成列表，每个元素只保留一个成分名称。\n"
            "2. 修正明显识别错误，但不要凭空补充图片中不存在的成分。\n"
            "3. 去掉剂量、百分比、括号中的解释性描述（除非括号本身是名称的一部分）。\n"
            "4. 只返回 JSON。\n"
            "5. JSON 格式固定为：{\"ingredients\": [\"水\", \"白砂糖\", \"柠檬酸\"]}\n"
        )

    @staticmethod
    def _text_only_prompt() -> str:
        return (
            "你是一个专业的食品标签文字提取助手。请尽可能完整提取图片中的可见文字内容。"
            "重点保留标签、包装、配料、产品名称、保存方式、致敏原、生产信息等文本。"
            "不要解释，不要总结，不要补充，只返回 JSON。\n"
            "JSON 格式固定为："
            "{\"raw_text\": \"这里放提取出的完整文字，保持自然换行或空格即可\"}"
        )

    @staticmethod
    def _layout_prompt() -> str:
        return (
            "你是一个香港食品标签审校助手。请阅读整张标签图片，并输出一个“接近原图排版”的结构化文字稿。"
            "你的目标不是逐字逐坐标还原，而是按照图片里的阅读顺序，把主要文字内容整理成多个文本块，"
            "并同时给出原始版本与香港繁体建议版本。\n\n"
            "请严格输出 JSON，不要输出 Markdown，不要输出解释。\n\n"
            "输出格式固定为：\n"
            "{\n"
            '  "blocks": [\n'
            "    {\n"
            '      "role": "title_line | field | paragraph | footer",\n'
            '      "label_original": "字段名原文，可为空",\n'
            '      "label_hk": "字段名香港繁体建议，可为空",\n'
            '      "value_original": "字段值原文，可为空",\n'
            '      "value_hk": "字段值香港繁体建议，可为空",\n'
            '      "original_text": "如果不是字段型，可直接放整行原文",\n'
            '      "hk_text": "对应的香港繁体建议整行"\n'
            "    }\n"
            "  ]\n"
            "}\n\n"
            "规则：\n"
            "1. 按图片的自然阅读顺序输出 blocks。\n"
            "2. 如果是一组“字段名: 内容”，优先使用 role=field，并分别填 label_original、label_hk、value_original、value_hk。\n"
            "3. 如果是一整行标题，使用 role=title_line。\n"
            "4. 如果是一整段说明文字，使用 role=paragraph。\n"
            "5. 如果是底部信息（如日期、地址、电话、标准号），可用 role=footer。\n"
            "6. hk_text / label_hk / value_hk 需转换成香港繁体表达，必要时可把“信息”改为“資訊”、“贮存”改为“貯存”等更符合香港习惯的写法。\n"
            "7. 尽量保留原始层次和阅读感，不要求像 OCR 一样返回坐标。\n"
            "8. 只返回 JSON。"
        )

    @staticmethod
    def _extract_json_block(text: str) -> Optional[str]:
        text = text.strip()

        fenced = re.search(r"```(?:json)?\s*(\{.*?\}|\[.*?\])\s*```", text, flags=re.S)
        if fenced:
            return fenced.group(1)

        obj_match = re.search(r"(\{.*\})", text, flags=re.S)
        if obj_match:
            return obj_match.group(1)

        arr_match = re.search(r"(\[.*\])", text, flags=re.S)
        if arr_match:
            return arr_match.group(1)

        return None

    @staticmethod
    def _clean_ingredient(value: str) -> str:
        value = str(value).strip().strip("，,;；。.")
        value = re.sub(r"^[\-•·\s]+", "", value)
        return value.strip()

    def _call_model(self, image_path: str, prompt_text: str):
        if not self.api_key:
            raise RuntimeError("未设置 DASHSCOPE_API_KEY 环境变量")

        if not os.path.exists(image_path):
            raise FileNotFoundError("图片文件不存在")

        response = MultiModalConversation.call(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"image": f"file://{os.path.abspath(image_path)}"},
                        {"text": prompt_text},
                    ],
                }
            ],
        )
        return response

    def _get_text_response(self, response):
        if response.status_code != 200:
            raise RuntimeError(
                f"API 调用失败：{getattr(response, 'code', '')} {getattr(response, 'message', '')}".strip()
            )

        try:
            return response.output.choices[0].message.content[0]["text"]
        except Exception as exc:
            raise RuntimeError(f"无法解析模型返回结果：{exc}") from exc

    def _parse_ingredient_response(self, text_response: str) -> ExtractionResult:
        json_text = self._extract_json_block(text_response) or text_response

        try:
            data = json.loads(json_text)
        except json.JSONDecodeError as exc:
            return ExtractionResult(
                success=False,
                raw_text=text_response,
                error=f"模型返回内容不是合法 JSON：{exc}",
            )

        if isinstance(data, dict):
            raw_items = data.get("ingredients", [])
        elif isinstance(data, list):
            raw_items = data
        else:
            raw_items = []

        ingredients: List[str] = []
        seen = set()

        for item in raw_items:
            if not isinstance(item, str):
                continue
            cleaned = self._clean_ingredient(item)
            if cleaned and cleaned not in seen:
                ingredients.append(cleaned)
                seen.add(cleaned)

        if not ingredients:
            return ExtractionResult(
                success=False,
                raw_text=text_response,
                error="模型未返回有效成分列表",
            )

        return ExtractionResult(success=True, ingredients=ingredients, raw_text=text_response)

    def _parse_text_only_response(self, text_response: str) -> TextOnlyResult:
        json_text = self._extract_json_block(text_response) or text_response

        try:
            data = json.loads(json_text)
        except json.JSONDecodeError:
            cleaned = text_response.strip()
            if cleaned:
                return TextOnlyResult(success=True, raw_text=cleaned)
            return TextOnlyResult(success=False, error="模型未返回有效文字内容")

        raw_text = ""
        if isinstance(data, dict):
            raw_text = str(data.get("raw_text", "")).strip()
        elif isinstance(data, str):
            raw_text = data.strip()

        if not raw_text:
            return TextOnlyResult(success=False, error="模型未返回有效文字内容")

        return TextOnlyResult(success=True, raw_text=raw_text)

    def _parse_layout_response(self, text_response: str) -> LayoutResult:
        json_text = self._extract_json_block(text_response) or text_response

        try:
            data = json.loads(json_text)
        except json.JSONDecodeError as exc:
            return LayoutResult(
                success=False,
                raw_text=text_response,
                error=f"模型返回内容不是合法 JSON：{exc}",
            )

        blocks_raw = []
        if isinstance(data, dict):
            blocks_raw = data.get("blocks", [])
        elif isinstance(data, list):
            blocks_raw = data

        blocks: List[LayoutBlock] = []

        for item in blocks_raw:
            if not isinstance(item, dict):
                continue

            role = str(item.get("role", "paragraph") or "paragraph").strip()
            block = LayoutBlock(
                role=role,
                label_original=str(item.get("label_original", "") or "").strip(),
                label_hk=str(item.get("label_hk", "") or "").strip(),
                value_original=str(item.get("value_original", "") or "").strip(),
                value_hk=str(item.get("value_hk", "") or "").strip(),
                original_text=str(item.get("original_text", "") or "").strip(),
                hk_text=str(item.get("hk_text", "") or "").strip(),
            )
            if (
                block.label_original
                or block.value_original
                or block.original_text
                or block.label_hk
                or block.value_hk
                or block.hk_text
            ):
                blocks.append(block)

        if not blocks:
            return LayoutResult(
                success=False,
                raw_text=text_response,
                error="模型未返回有效版式文本块",
            )

        return LayoutResult(success=True, blocks=blocks, raw_text=text_response)

    def extract(self, image_path: str) -> ExtractionResult:
        try:
            response = self._call_model(image_path, self._ingredient_prompt())
            text_response = self._get_text_response(response)
            return self._parse_ingredient_response(text_response)
        except Exception as exc:
            return ExtractionResult(success=False, error=f"模型调用异常：{exc}")

    def extract_text_only(self, image_path: str) -> TextOnlyResult:
        try:
            response = self._call_model(image_path, self._text_only_prompt())
            text_response = self._get_text_response(response)
            return self._parse_text_only_response(text_response)
        except Exception as exc:
            return TextOnlyResult(success=False, error=f"模型调用异常：{exc}")

    def extract_layout_text(self, image_path: str) -> LayoutResult:
        try:
            response = self._call_model(image_path, self._layout_prompt())
            text_response = self._get_text_response(response)
            return self._parse_layout_response(text_response)
        except Exception as exc:
            return LayoutResult(success=False, error=f"模型调用异常：{exc}")