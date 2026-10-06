"""
Multi-tradition ethical and metaphysical filters.
Excluded by explicit user request: Islam and Judaism.
All other listed traditions are used only as research heuristics.
"""

from typing import Tuple, Dict

# Allowed research traditions (user-specified exclusions applied)
TRADITIONS: Tuple[str, ...] = (
    "I_CHING",
    "BA_ZI",
    "LAO_TZU",
    "SUN_TZU",
    "SLAVIC_VEDA",
    "INGLIISM",
    "CHRISTIANITY",          # compassion, love, non-harm
    "SHAMANISM",
    "GUNAS",
    "VEDANTA",
    "TAOISM",
    "QI_GONG",
    "TANTRA_ETHICS",         # only non-sexual ethical aspects
    "HERMETICISM",
    "NOOSPHERE",
    "UNCERTAINTY",
)

GUNAS = ("SATTVA", "RAJAS", "TAMAS")

VIRTUES: Dict[str, float] = {
    "love": 0.90,            # приумножение жизни
    "wisdom": 0.82,
    "faith": 0.70,
    "hope": 0.68,
    "will": 0.85,
    "compassion": 0.88,
    "freedom": 0.80,
    "non_harm": 0.95,        # hard priority
    "protection_of_life": 1.0,
}

# Golden Ratio used only as soft dynamical constant
PHI = 1.6180339887498948
PHI_INV = 1.0 / PHI
GOLDEN_MEAN = PHI_INV
