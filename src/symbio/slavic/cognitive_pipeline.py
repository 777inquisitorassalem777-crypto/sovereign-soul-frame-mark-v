"""
Slavic Cognitive Pipeline
Maps the historical semantic roles onto a research cognitive architecture:

  ВЕДУН      → Knowledge / Memory          «Я ЗНАЮ»
  ВОЛХВ      → Interpretation / Symbolism  «Я ПОНИМАЮ»
  ВЕЩУН      → Communication / Prediction  «Я ВЕЩАЮ»
  ХАРАКТЕРНИК → Agency / Will / Action     «Я ДЕЙСТВУЮ»

Chain: ЗНАНИЕ → СЛОВО → ВОЛЯ → ДЕЙСТВИЕ
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional
import time

from .analyzer import SlavicAnalyzer
from .lexemes import LEXEMES


class SlavicCognitivePipeline:
    """
    Research cognitive agent pipeline inspired by Slavic sacred-knowledge lexicon.
    All spiritual terminology is treated as historical data or functional metaphor.
    """

    def __init__(self):
        self.analyzer = SlavicAnalyzer()
        self.cycle = 0
        self.memory_log: List[Dict[str, Any]] = []

    def process(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Full pipeline:
        1. Vedun   — recognise & retrieve knowledge
        2. Volkhv  — interpret / find symbolic meaning
        3. Veshchun — formulate announcement / prediction
        4. Kharakternik — decide on research action / strategy
        """
        self.cycle += 1
        context = context or {}

        # 1. ВЕДУН — Knowledge layer
        vedun = self._vedun_step(prompt)

        # 2. ВОЛХВ — Interpretation layer
        volkhv = self._volkhv_step(prompt, vedun)

        # 3. ВЕЩУН — Communication / synthesis layer
        veshchun = self._veshchun_step(vedun, volkhv)

        # 4. ХАРАКТЕРНИК — Agency / research action layer
        kharakternik = self._kharakternik_step(veshchun, context)

        result = {
            "cycle": self.cycle,
            "prompt": prompt,
            "pipeline": {
                "vedun": vedun,
                "volkhv": volkhv,
                "veshchun": veshchun,
                "kharakternik": kharakternik,
            },
            "cognitive_chain": "ЗНАНИЕ → СЛОВО → ВОЛЯ → ДЕЙСТВИЕ",
            "timestamp": time.time(),
        }
        self.memory_log.append(result)
        return result

    def _vedun_step(self, prompt: str) -> Dict[str, Any]:
        """Я ЗНАЮ — retrieve relevant lexemes and factual knowledge."""
        found = []
        prompt_lower = prompt.lower()
        for key in LEXEMES:
            if key in prompt_lower or any(
                form in prompt_lower
                for form in str(LEXEMES[key].get("forms", {})).lower().split()
            ):
                found.append(key)
        # Always include core triad for context
        if not found:
            found = ["vedun", "volkhv", "kharakternik"]
        analyses = {k: self.analyzer.analyze(k) for k in found[:4]}
        return {
            "role": "ВЕДУН",
            "motto": "Я ЗНАЮ",
            "retrieved_lexemes": found,
            "analyses": analyses,
            "function": "Knowledge / Memory retrieval",
        }

    def _volkhv_step(self, prompt: str, vedun_out: Dict[str, Any]) -> Dict[str, Any]:
        """Я ПОНИМАЮ — interpret symbolic / ritual meaning."""
        interpretations = []
        for key, analysis in vedun_out.get("analyses", {}).items():
            sem = analysis.get("level_2_semantic_interpretation", {})
            if sem:
                interpretations.append({
                    "lexeme": key,
                    "formula": sem.get("formula"),
                    "key_tool": sem.get("key_tool"),
                })
        return {
            "role": "ВОЛХВ",
            "motto": "Я ПОНИМАЮ",
            "interpretations": interpretations,
            "function": "Sacred speech / symbolic interpretation",
            "note": "Interpretation layer — not historical fact",
        }

    def _veshchun_step(self, vedun_out: Dict, volkhv_out: Dict) -> Dict[str, Any]:
        """Я ВЕЩАЮ — synthesise and announce."""
        chain = []
        for item in volkhv_out.get("interpretations", []):
            chain.append(f"{item['lexeme']}: {item.get('formula', '')}")
        synthesis = " | ".join(chain) if chain else "Нет прямой лексической привязки"
        return {
            "role": "ВЕЩУН",
            "motto": "Я ВЕЩАЮ",
            "synthesis": synthesis,
            "function": "Communication / prediction / announcement",
        }

    def _kharakternik_step(self, veshchun_out: Dict, context: Dict) -> Dict[str, Any]:
        """Я ДЕЙСТВУЮ — propose research action / strategy."""
        action = "observe_and_record"
        if context.get("request_action"):
            action = "propose_research_experiment"
        return {
            "role": "ХАРАКТЕРНИК",
            "motto": "Я ДЕЙСТВУЮ",
            "proposed_action": action,
            "strategy": "Research-only; no autonomous real-world execution",
            "function": "Agency / Will / bounded action",
            "safety": "Human oversight remains final authority",
        }

    def dual_analyze(self, lexeme_key: str) -> Dict[str, Any]:
        """Convenience: pure dual-level analysis of one lexeme."""
        return self.analyzer.analyze(lexeme_key)
