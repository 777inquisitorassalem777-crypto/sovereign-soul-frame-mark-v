"""
Ritual Structure Analyzer — research only.
Describes historical/folkloric structures. Does NOT provide operational instructions.
"""

from __future__ import annotations

from typing import Any, Dict, List

from .catalog import (
    SYMBOLS,
    RITUAL_STRUCTURES,
    get_symbol,
    get_ritual,
    list_symbols,
    list_rituals,
    SymbolStatus,
)


class RitualStructureAnalyzer:
    """
    Returns structured information about symbols and ritual patterns.
    All output is descriptive and research-oriented.
    """

    def describe_symbol(self, key: str) -> Dict[str, Any]:
        data = get_symbol(key)
        if not data:
            return {"error": f"Unknown symbol: {key}", "available": list_symbols()}
        return {
            "key": key,
            "name_ru": data.get("name_ru"),
            "status": data.get("status"),
            "description": data.get("description"),
            "historical_note": data.get("historical_note"),
            "associations": data.get("associations", []),
            "disclaimer": (
                "Research description only. "
                "Status indicates degree of historical attestation."
            ),
        }

    def describe_ritual(self, key: str) -> Dict[str, Any]:
        data = get_ritual(key)
        if not data:
            return {"error": f"Unknown ritual structure: {key}", "available": list_rituals()}
        return {
            "key": key,
            "name_ru": data.get("name_ru"),
            "status": data.get("status"),
            "description": data.get("description"),
            "structure": data.get("structure", []),
            "attested_examples": data.get("attested_examples"),
            "note": data.get("note"),
            "disclaimer": (
                "This is a structural description of historical/folkloric patterns. "
                "It is not an instruction for performing any ritual."
            ),
        }

    def list_all_symbols(self) -> List[Dict[str, str]]:
        return [
            {
                "key": k,
                "name_ru": v.get("name_ru"),
                "status": str(v.get("status")),
            }
            for k, v in SYMBOLS.items()
        ]

    def list_all_rituals(self) -> List[Dict[str, str]]:
        return [
            {
                "key": k,
                "name_ru": v.get("name_ru"),
                "status": str(v.get("status")),
            }
            for k, v in RITUAL_STRUCTURES.items()
        ]

    def enrich_lexeme(self, lexeme_key: str) -> Dict[str, Any]:
        """
        Suggest related symbols/rituals for a lexeme (interpretive layer).
        """
        mapping = {
            "volkhv": {
                "symbols": ["world_tree", "ogle_fire", "solar_rosette"],
                "rituals": ["calendar_rite", "sacrifice_offering"],
                "note": "Волхв как носитель ритуального слова и посредник",
            },
            "vedun": {
                "symbols": ["bereginya", "water_boundary"],
                "rituals": ["healing_charm", "ancestor_communion"],
                "note": "Ведун как обладатель знания о скрытом и целебном",
            },
            "kharakternik": {
                "symbols": ["perun_axe"],
                "rituals": ["warrior_protection"],
                "note": "Поздний воинский пласт; связь с защитой и неуязвимостью",
            },
        }
        return mapping.get(lexeme_key, {"symbols": [], "rituals": [], "note": "No direct mapping"})
