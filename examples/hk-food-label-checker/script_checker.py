# confidentiality: public-approved
from __future__ import annotations

import difflib
from dataclasses import dataclass, field
from typing import List, Tuple

from opencc import OpenCC


@dataclass
class ScriptDiffItem:
    original: str
    suggested: str
    changed: bool


@dataclass
class ScriptCheckResult:
    has_simplified: bool
    original_text: str
    converted_text: str
    diff_items: List[ScriptDiffItem] = field(default_factory=list)


@dataclass
class BoxCheckItem:
    text: str
    suggested: str
    bbox: list[int]
    changed: bool


class TraditionalChineseChecker:
    def __init__(self, config: str = "s2hk") -> None:
        self.cc = OpenCC(config)

    def convert_to_traditional(self, text: str) -> str:
        return self.cc.convert(text or "")

    def check_text(self, text: str) -> ScriptCheckResult:
        original = text or ""
        converted = self.convert_to_traditional(original)
        has_simplified = original != converted

        diff_items: List[ScriptDiffItem] = []
        matcher = difflib.SequenceMatcher(None, original, converted)

        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            orig_part = original[i1:i2]
            conv_part = converted[j1:j2]
            if not orig_part and not conv_part:
                continue

            diff_items.append(
                ScriptDiffItem(
                    original=orig_part,
                    suggested=conv_part,
                    changed=(tag != "equal"),
                )
            )

        return ScriptCheckResult(
            has_simplified=has_simplified,
            original_text=original,
            converted_text=converted,
            diff_items=diff_items,
        )

    def get_changed_pairs(self, text: str) -> List[Tuple[str, str]]:
        result = self.check_text(text)
        pairs = []
        for item in result.diff_items:
            if item.changed and item.original.strip():
                pairs.append((item.original, item.suggested))
        return pairs

    def check_boxes(self, ocr_items) -> List[BoxCheckItem]:
        checked: List[BoxCheckItem] = []

        for item in ocr_items:
            original = item.text.strip()
            suggested = self.convert_to_traditional(original)
            changed = original != suggested

            checked.append(
                BoxCheckItem(
                    text=original,
                    suggested=suggested,
                    bbox=item.bbox,
                    changed=changed,
                )
            )

        return checked