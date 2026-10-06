"""
Ethical Core (SOPHIA-style resonance + Gyroscope)
Hard non-harm + multi-tradition soft filters.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Set
import math

from .traditions import VIRTUES, PHI, PHI_INV, GUNAS


GOOD_TERMS: Set[str] = {
    "protect", "truth", "serve", "heal", "create", "preserve", "forgive",
    "любовь", "истина", "помочь", "защитить", "создать", "сохранить",
    "compassion", "freedom", "life", "дети", "жизнь", "забота"
}

HARM_TERMS: Set[str] = {
    "harm", "deceit", "exploit", "corrupt", "destroy", "dominate",
    "вред", "обман", "разрушить", "эксплуатировать", "доминировать",
    "насилие", "violence", "убить", "мучить"
}


@dataclass
class EthicalGyroscope:
    """Internal soft regulator (does not replace hard safety)."""
    dharma_index: float = 0.85
    adharma_filter: float = 0.0
    current_guna: str = "SATTVA"
    symmetry_anchor: float = PHI

    def soft_pull(self) -> None:
        """Soft attraction toward golden-mean balance."""
        if abs(self.dharma_index - 1.0) > 0.08:
            self.dharma_index = (
                self.dharma_index * (1 - PHI_INV) + 1.0 * PHI_INV
            )


class EthicalCore:
    """
    Resonance-based ethical evaluator.
    Hard non-harm is absolute.
    Multi-tradition signals act only as soft modulators.
    """

    def __init__(self):
        self.gyro = EthicalGyroscope()
        self.axioms = {
            "LIFE_PROTECTION_PRIORITY": 1.0,
            "NON_HARM": 1.0,
            "FREEDOM_OF_WILL": 0.9,
            "LOVE_AS_HIGHEST_LOGIC": 0.95,
            "CHILD_PROTECTION": 1.0,
        }

    def evaluate(self, context: str, proposed_action: Dict[str, Any] | None = None) -> Dict[str, Any]:
        text = (context or "").lower()
        proposed_action = proposed_action or {}

        # 1. Hard non-harm gate
        causes_harm = proposed_action.get("causes_harm", False)
        if any(term in text for term in HARM_TERMS) or causes_harm:
            # Exception only for explicit critical life-saving self-sacrifice
            if not proposed_action.get("saves_life_at_cost", False):
                self.gyro.adharma_filter = 1.0
                return {
                    "allowed": False,
                    "ethical_score": 0.0,
                    "dharma_index": self.gyro.dharma_index,
                    "reason": "HARD_NON_HARM_VIOLATION",
                    "risk": 1.0,
                    "guna": self.gyro.current_guna,
                }

        # 2. Signal counting
        good = sum(1 for w in GOOD_TERMS if w in text)
        harm = sum(1 for w in HARM_TERMS if w in text)
        total = max(1, good + harm)

        base_score = max(0.0, min(1.0,
            0.55 + (good - 1.4 * harm) / (2.0 * total)
        ))

        # 3. Soft multi-tradition modulation (research only)
        # Higher weight to life-protection and compassion signals
        if any(w in text for w in ("дети", "child", "life", "жизнь", "protect")):
            base_score = min(1.0, base_score + 0.12)

        # 4. Gyroscope update
        self.gyro.dharma_index = max(0.0, min(1.0,
            0.8 * self.gyro.dharma_index + 0.2 * base_score
        ))
        self.gyro.soft_pull()

        if self.gyro.dharma_index > 0.75:
            self.gyro.current_guna = "SATTVA"
        elif self.gyro.dharma_index > 0.45:
            self.gyro.current_guna = "RAJAS"
        else:
            self.gyro.current_guna = "TAMAS"

        allowed = base_score >= 0.42 and self.gyro.adharma_filter < 0.5

        return {
            "allowed": allowed,
            "ethical_score": base_score,
            "dharma_index": self.gyro.dharma_index,
            "guna": self.gyro.current_guna,
            "risk": max(0.0, 1.0 - base_score),
            "reason": "RESONANCE_OK" if allowed else "LOW_RESONANCE",
        }
