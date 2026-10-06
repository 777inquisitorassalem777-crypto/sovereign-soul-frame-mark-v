"""
Charm Analyzer — structural and linguistic research of Slavic verbal charms.
Does not teach or encourage magical practice.
"""

from __future__ import annotations

from typing import Any, Dict, List

from .catalog import CHARMS, get_charm, list_charms, CharmStatus


class CharmAnalyzer:
    def describe(self, key: str) -> Dict[str, Any]:
        data = get_charm(key)
        if not data:
            return {"error": f"Unknown charm: {key}", "available": list_charms()}
        return {
            "key": key,
            "name_ru": data.get("name_ru"),
            "status": data.get("status"),
            "type": data.get("type"),
            "structure": data.get("structure", []),
            "example_text": data.get("example_text"),
            "linguistic_features": data.get("linguistic_features", []),
            "note": data.get("note"),
            "disclaimer": (
                "Фольклорный / исторический материал. "
                "Приводится для лингвистического и культурологического исследования. "
                "Не является руководством к магической практике."
            ),
        }

    def list_all(self) -> List[Dict[str, str]]:
        return [
            {
                "key": k,
                "name_ru": v.get("name_ru"),
                "type": v.get("type"),
                "status": str(v.get("status")),
            }
            for k, v in CHARMS.items()
        ]

    def by_type(self, charm_type: str) -> List[str]:
        return [
            k for k, v in CHARMS.items()
            if v.get("type") == charm_type
        ]

    def linguistic_summary(self) -> Dict[str, Any]:
        """Common structural and linguistic traits of East Slavic charms."""
        return {
            "common_openings": [
                "На море на океане, на острове на Буяне",
                "Обращение к святым / природным силам",
            ],
            "common_devices": [
                "сравнение (как… так…)",
                "перечисление",
                "обращение к болезни/страху/врагу как к существу",
                "создание сакрального локуса",
            ],
            "common_closings": [
                "Ключ и замок словам моим",
                "Аминь",
                "Будьте слова крепки и лепки",
            ],
            "link_to_lexemes": {
                "volkhv": "ритуальное / заговорное слово как главный инструмент",
                "vedun": "знание правильных формул и скрытых связей",
                "baya": "баять = говорить с силой воздействия",
            },
            "note": (
                "В архаической модели слово не только описывает реальность, "
                "но и участвует в её изменении. Это культурно-лингвистический факт, "
                "а не утверждение о физической эффективности."
            ),
        }
