"""Sovereign Soul Frame — Mark V symbiotic package."""

from .soul_core import SoulCore, EthicalGyroscope, SoulSignature
from .authority_gate import AuthorityGate
from .embodiment import EmbodimentInterface
from .hardware_map import HARDWARE_MAP, get_system_info, list_all_systems

__all__ = [
    "SoulCore",
    "EthicalGyroscope",
    "SoulSignature",
    "AuthorityGate",
    "EmbodimentInterface",
    "HARDWARE_MAP",
    "get_system_info",
    "list_all_systems",
]
