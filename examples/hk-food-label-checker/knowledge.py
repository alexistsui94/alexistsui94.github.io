# confidentiality: public-approved
from __future__ import annotations

import difflib
import os
import re
from dataclasses import dataclass
from typing import Dict, Optional, Set

import pandas as pd


@dataclass
class LookupResult:
    found: bool
    is_additive: bool = False
    is_common_food: bool = False

    additive_id: str = ""
    name: str = ""              # 默认展示名，优先简体
    name_zh_cn: str = ""
    name_zh_hk: str = ""
    name_en: str = ""

    e_code: str = ""
    e_code_norm: str = ""

    func_zh: str = ""           # 默认展示功能，优先简体
    func_zh_cn: str = ""
    func_zh_hk: str = ""
    func_en: str = ""
    function_codes: str = ""
    category_primary: str = ""

    match_type: str = ""        # exact / alias / e_number / fuzzy / common_food
    matched_on: str = ""
    score: float = 1.0

    notes: str = ""
    alias_type: str = ""


class KnowledgeBase:
    def __init__(self, file_path: str = "demo_knowledge.xlsx") -> None:
        self.file_path = file_path

        self.master_df: Optional[pd.DataFrame] = None
        self.alias_df: Optional[pd.DataFrame] = None
        self.common_df: Optional[pd.DataFrame] = None

        self.master_name_map: Dict[str, pd.Series] = {}
        self.alias_map: Dict[str, tuple[pd.Series, pd.Series]] = {}
        self.e_number_map: Dict[str, pd.Series] = {}
        self.common_food_set: Set[str] = set()

        self.load_data()

    @staticmethod
    def _safe_text(value: object) -> str:
        if value is None:
            return ""
        try:
            if pd.isna(value):
                return ""
        except Exception:
            pass
        text = str(value).strip()
        return "" if text.lower() == "nan" else text

    @staticmethod
    def _normalize_text(text: str) -> str:
        text = str(text or "").strip().lower()

        # 全角/变体统一
        text = (
            text.replace("（", "(")
            .replace("）", ")")
            .replace("【", "[")
            .replace("】", "]")
            .replace("’", "'")
            .replace("′", "'")
            .replace("＇", "'")
            .replace("－", "-")
            .replace("—", "-")
            .replace("–", "-")
        )

        # 常见繁简字符轻量归一
        replacements = {
            "鈉": "钠",
            "鉀": "钾",
            "鈣": "钙",
            "鎂": "镁",
            "鋅": "锌",
            "鐵": "铁",
            "銅": "铜",
            "錳": "锰",
            "檸": "柠",
            "黃": "黄",
            "膠": "胶",
            "鹽": "盐",
            "穩": "稳",
            "劑": "剂",
            "調": "调",
            "節": "节",
            "酸度調節劑": "酸度调节剂",
            "增稠劑": "增稠剂",
            "乳化劑": "乳化剂",
            "抗氧化劑": "抗氧化剂",
            "防腐劑": "防腐剂",
            "甜味劑": "甜味剂",
            "著色劑": "着色剂",
            "色素": "着色剂",
            "穀": "谷",
            "麩": "麸",
        }
        for old, new in replacements.items():
            text = text.replace(old.lower(), new.lower())

        # 去空白
        text = re.sub(r"\s+", "", text)

        # 统一 5'- 这类写法
        text = text.replace("5’-", "5'-").replace("5′-", "5'-")

        return text.strip()

    @staticmethod
    def _normalize_e_number(text: str) -> str:
        text = str(text or "").strip().lower()
        text = text.replace("（", "(").replace("）", ")")
        text = re.sub(r"\s+", "", text)

        # 335(ii) -> e335ii
        # E335(ii) -> e335ii
        # e 102 -> e102
        if not text:
            return ""

        if not text.startswith("e"):
            # 像 335(ii) 这种
            if re.match(r"^\d+[a-z]?(?:\([ivx]+\))?$", text):
                text = "e" + text

        text = text.replace("(", "").replace(")", "")
        return text

    def load_data(self) -> None:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"未找到知识库文件：{self.file_path}")

        self.master_df = pd.read_excel(self.file_path, sheet_name="additives_master")
        self.alias_df = pd.read_excel(self.file_path, sheet_name="additives_aliases")
        self.common_df = pd.read_excel(self.file_path, sheet_name="common_non_additives")

        for df in [self.master_df, self.alias_df, self.common_df]:
            for col in df.columns:
                if df[col].dtype == "object":
                    df[col] = df[col].fillna("").astype(str).str.strip()

        self.master_name_map.clear()
        self.alias_map.clear()
        self.e_number_map.clear()
        self.common_food_set.clear()

        # 主表索引
        for _, row in self.master_df.iterrows():
            name_cn = self._safe_text(row.get("canonical_name_zh_cn", ""))
            name_hk = self._safe_text(row.get("canonical_name_zh_hk", ""))
            e_number = self._safe_text(row.get("e_number", ""))
            e_number_norm = self._safe_text(row.get("e_number_norm", ""))

            for name in [name_cn, name_hk]:
                if name:
                    key = self._normalize_text(name)
                    if key and key not in self.master_name_map:
                        self.master_name_map[key] = row

            for e in [e_number, e_number_norm]:
                if e:
                    key = self._normalize_e_number(e)
                    if key and key not in self.e_number_map:
                        self.e_number_map[key] = row

        # 先做 additive_id -> master row 映射
        master_by_id: Dict[str, pd.Series] = {}
        for _, row in self.master_df.iterrows():
            additive_id = self._safe_text(row.get("additive_id", ""))
            if additive_id:
                master_by_id[additive_id] = row

        # 别名索引
        for _, alias_row in self.alias_df.iterrows():
            alias_text = self._safe_text(alias_row.get("alias_text", ""))
            alias_type = self._safe_text(alias_row.get("alias_type", ""))
            additive_id = self._safe_text(alias_row.get("additive_id", ""))

            if not alias_text or not additive_id:
                continue

            master_row = master_by_id.get(additive_id)
            if master_row is None:
                continue

            if alias_type == "e_number":
                key = self._normalize_e_number(alias_text)
            else:
                key = self._normalize_text(alias_text)

            if key and key not in self.alias_map:
                self.alias_map[key] = (master_row, alias_row)

        # 普通配料词表
        for _, row in self.common_df.iterrows():
            name = self._safe_text(row.get("name", ""))
            name_norm = self._safe_text(row.get("name_norm", ""))

            for value in [name, name_norm]:
                if value:
                    key = self._normalize_text(value)
                    if key:
                        self.common_food_set.add(key)

    def _format_result(
        self,
        row: pd.Series,
        *,
        match_type: str,
        matched_on: str,
        score: float = 1.0,
        alias_type: str = "",
        is_common_food: bool = False,
    ) -> LookupResult:
        name_cn = self._safe_text(row.get("canonical_name_zh_cn", ""))
        name_hk = self._safe_text(row.get("canonical_name_zh_hk", ""))
        func_cn = self._safe_text(row.get("function_zh_cn", ""))
        func_hk = self._safe_text(row.get("function_zh_hk", ""))

        return LookupResult(
            found=True,
            is_additive=not is_common_food,
            is_common_food=is_common_food,
            additive_id=self._safe_text(row.get("additive_id", "")),
            name=name_cn or name_hk,
            name_zh_cn=name_cn,
            name_zh_hk=name_hk,
            name_en=self._safe_text(row.get("canonical_name_en", "")),
            e_code=self._safe_text(row.get("e_number", "")),
            e_code_norm=self._safe_text(row.get("e_number_norm", "")),
            func_zh=func_cn or func_hk,
            func_zh_cn=func_cn,
            func_zh_hk=func_hk,
            func_en=self._safe_text(row.get("function_en", "")),
            function_codes=self._safe_text(row.get("function_codes", "")),
            category_primary=self._safe_text(row.get("category_primary", "")),
            match_type=match_type,
            matched_on=matched_on,
            score=score,
            notes=self._safe_text(row.get("notes", "")),
            alias_type=alias_type,
        )

    def _format_common_food_result(self, ingredient_name: str) -> LookupResult:
        return LookupResult(
            found=False,
            is_additive=False,
            is_common_food=True,
            name=ingredient_name,
            match_type="common_food",
            matched_on=ingredient_name,
        )

    def _get_fuzzy_candidates(self) -> Dict[str, pd.Series]:
        candidates: Dict[str, pd.Series] = {}

        for key, row in self.master_name_map.items():
            candidates[key] = row

        for key, (master_row, alias_row) in self.alias_map.items():
            allow_fuzzy = alias_row.get("is_fuzzy_candidate", False)
            try:
                allow_fuzzy = self._safe_text(allow_fuzzy).lower() in {"true", "1", "yes"}
            except Exception:
                allow_fuzzy = False

            if allow_fuzzy and key not in candidates:
                candidates[key] = master_row

        return candidates

    def get_info(self, ingredient_name: str, fuzzy_cutoff: float = 0.86) -> LookupResult:
        raw = str(ingredient_name or "").strip()
        if not raw:
            return LookupResult(found=False)

        key_text = self._normalize_text(raw)
        key_e = self._normalize_e_number(raw)

        # 1) 普通配料先拦截
        if key_text in self.common_food_set:
            return self._format_common_food_result(raw)

        # 2) 主名精确匹配
        row = self.master_name_map.get(key_text)
        if row is not None:
            return self._format_result(
                row,
                match_type="exact",
                matched_on=raw,
            )

        # 3) E 编号匹配
        if key_e:
            row = self.e_number_map.get(key_e)
            if row is not None:
                return self._format_result(
                    row,
                    match_type="e_number",
                    matched_on=raw,
                )

        # 4) 别名精确匹配
        alias_hit = self.alias_map.get(key_text) or (self.alias_map.get(key_e) if key_e else None)
        if alias_hit is not None:
            master_row, alias_row = alias_hit
            return self._format_result(
                master_row,
                match_type="alias",
                matched_on=raw,
                alias_type=self._safe_text(alias_row.get("alias_type", "")),
            )

        # 5) 模糊匹配兜底
        fuzzy_candidates = self._get_fuzzy_candidates()
        best = difflib.get_close_matches(key_text, list(fuzzy_candidates.keys()), n=1, cutoff=fuzzy_cutoff)

        if best:
            best_key = best[0]
            row = fuzzy_candidates.get(best_key)
            if row is not None:
                score = difflib.SequenceMatcher(None, key_text, best_key).ratio()
                return self._format_result(
                    row,
                    match_type="fuzzy",
                    matched_on=raw,
                    score=score,
                )

        return LookupResult(found=False, matched_on=raw)

    def is_common_food(self, ingredient_name: str) -> bool:
        key = self._normalize_text(ingredient_name)
        return key in self.common_food_set

    def get_display_name(self, ingredient_name: str) -> str:
        info = self.get_info(ingredient_name)
        return info.name if info.found else ingredient_name