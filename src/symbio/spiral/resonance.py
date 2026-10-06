"""
Resonance Metric — research proxy for ethical / emotional alignment.
Not a claim of quantum consciousness.
"""

from __future__ import annotations

from typing import Dict, Any
import math
import random

from ..traditions import PHI, PHI_INV


class ResonanceMetric:
    """
    Soft continuous score instead of binary moral filter.
    Higher resonance → action is more aligned with life-multiplication,
    compassion and non-harm.
    """

    def __init__(self):
        self.baseline = 0.72          # "Universal Love Frequency" proxy
        self.history: list[float] = []

    def calculate(self, intent_vector: Dict[str, float]) -> float:
        """
        intent_vector expected keys (all 0..1):
          compassion, truth, creative_growth, harm_risk, freedom_support
        """
        compassion = intent_vector.get("compassion", 0.5)
        truth = intent_vector.get("truth", 0.5)
        creative = intent_vector.get("creative_growth", 0.5)
        harm = intent_vector.get("harm_risk", 0.0)
        freedom = intent_vector.get("freedom_support", 0.5)

        raw = (
            0.30 * compassion
            + 0.25 * truth
            + 0.20 * creative
            + 0.15 * freedom
            - 0.40 * harm
        )
        # Soft pull toward baseline with golden-ratio damping
        score = max(0.0, min(1.0, raw * 0.7 + self.baseline * 0.3))
        self.history.append(score)
        return score

    def find_harmonic_alternative(self, original_score: float) -> float:
        """Suggest a higher-resonance path (research heuristic)."""
        return min(1.0, original_score + 0.15 * PHI_INV + random.uniform(0, 0.08))

    def recalibrate(self) -> None:
        """Return toward baseline after ethical stress."""
        if self.history:
            self.baseline = 0.6 * self.baseline + 0.4 * (sum(self.history[-5:]) / min(5, len(self.history)))
        self.baseline = max(0.5, min(0.9, self.baseline))
