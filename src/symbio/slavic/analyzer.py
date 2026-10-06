"""
Dual-level Slavic Analyzer.
Never mixes historical-linguistic FACT with INTERPRETATION in the same output block.
"""

from __future__ import annotations

from typing import Any, Dict, List

from .lexemes import LEXEMES, LexemeStatus, get_lexeme


class SlavicAnalyzer:
    """
    Performs strict dual-level analysis of a Slavic sacred-knowledge lexeme.
    """

    def analyze(self, key: str) -> Dict[str, Any]:
        data = get_lexeme(key)
        if not data:
            return {
                "error": f"Unknown lexeme: {key}",
                "available": list(LEXEMES.keys()),
            }

        # Level 1 — Historical-linguistic (FACT / HYPOTHESIS / DISPUTED only)
        historical = {
            "forms": data.get("forms", {}),
            "etymology": {},
            "period": data.get("period"),
        }
        for ety_key, ety_val in data.get("etymology", {}).items():
            if isinstance(ety_val, dict) and ety_val.get("status") in (
                LexemeStatus.FACT,
                LexemeStatus.HYPOTHESIS,
                LexemeStatus.DISPUTED,
            ):
                historical["etymology"][ety_key] = ety_val

        # Level 2 — Semantic / interpretive reconstruction
        semantic = data.get("semantic_core", {})
        # Force status to INTERPRETATION if present
        if semantic:
            semantic = {**semantic, "status": LexemeStatus.INTERPRETATION}

        return {
            "lexeme": key,
            "level_1_historical_linguistic": historical,
            "level_2_semantic_interpretation": semantic,
            "disclaimer": (
                "Level 1 contains only attested forms and scholarly etymology. "
                "Level 2 is modern semantic reconstruction and must not be "
                "presented as direct historical fact."
            ),
        }

    def compare(self, keys: List[str]) -> Dict[str, Any]:
        results = {k: self.analyze(k) for k in keys}
        return {
            "comparison": results,
            "cognitive_mapping_hint": {
                "vedun": "ЗНАНИЕ (Knowledge / Memory)",
                "volkhv": "СЛОВО + РИТУАЛ (Interpretation / Sacred Speech)",
                "veshchun": "ВЕЩАНИЕ (Communication / Prediction)",
                "kharakternik": "ВОЛЯ + ДЕЙСТВИЕ (Agency / Will / Action)",
            },
        }
