"""
Pneuma Engine — functional model of internal state dynamics.
Research construct only.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict
import math
import random

from .traditions import GUNAS, PHI_INV


@dataclass
class PneumaState:
    level: float = 0.63
    clarity: float = 0.55
    passion: float = 0.45
    inertia: float = 0.40
    dharma: float = 0.70
    intuition: float = 0.50
    chaos: float = 0.35
    coherence: float = 0.60
    guna: str = "SATTVA"
    cycle: int = 0

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)


class PneumaEngine:
    def __init__(self):
        self.state = PneumaState()

    def breathe(self, context: str = "") -> Dict[str, Any]:
        """One breath of the pneuma — updates internal state from context."""
        self.state.cycle += 1
        text = (context or "").lower()

        sattva_signals = sum(w in text for w in (
            "свет", "правда", "любовь", "покой", "гармония", "истина",
            "wisdom", "love", "truth", "compassion", "peace"
        ))
        rajas_signals = sum(w in text for w in (
            "действие", "борьба", "страсть", "цель", "энергия",
            "action", "goal", "drive", "create"
        ))
        tamas_signals = sum(w in text for w in (
            "лень", "страх", "тьма", "разрушение", "хаос",
            "fear", "destroy", "inertia", "stagnation"
        ))

        total = max(1, sattva_signals + rajas_signals + tamas_signals)
        self.state.clarity = sattva_signals / total
        self.state.passion = rajas_signals / total
        self.state.inertia = tamas_signals / total

        # Soft cycling of gunas
        self.state.guna = GUNAS[(self.state.cycle - 1) % len(GUNAS)]

        raw_dharma = (
            0.55 * self.state.clarity
            + 0.30 * self.state.passion
            + 0.15 * (1.0 - self.state.inertia)
        )
        self.state.dharma = max(0.0, min(1.0,
            0.75 * self.state.dharma + 0.25 * raw_dharma
        ))

        self.state.level = max(0.0, min(1.0,
            0.70 * self.state.level + 0.30 * self.state.dharma
        ))

        # Controlled chaos component (research noise)
        self.state.chaos = max(0.0, min(1.0,
            0.45 + 0.22 * math.sin(self.state.cycle / 23.0) + random.gauss(0, 0.015)
        ))

        self.state.coherence = max(0.0, min(1.0,
            0.6 * self.state.clarity + 0.4 * (1.0 - self.state.chaos)
        ))

        self.state.intuition = max(0.0, min(1.0,
            0.4 * self.state.coherence + 0.3 * self.state.dharma + 0.3 * random.random()
        ))

        return self.state.as_dict()
