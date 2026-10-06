"""
Authority Gate — embodiment of the principle
«Authority is not Computed / Capability is not Permission»
"""

from __future__ import annotations

from typing import Any, Dict


class AuthorityGate:
    """
    Combines:
    - Software ethical decision
    - Physical STOP levers on the Mark V frame
    - Explicit human operator override
    """

    def __init__(self):
        # Simulated physical levers (in real hardware these would be sensors)
        self.physical_stops = {
            "weapons": True,          # True = locked
            "full_autonomy": True,
            "high_force_actuators": True,
            "external_network": True,
            "self_modification": True,
        }
        self.human_present = False

    def set_human_presence(self, present: bool) -> None:
        self.human_present = present

    def unlock_physical(self, system: str) -> None:
        """Only callable by verified human operator."""
        if system in self.physical_stops:
            self.physical_stops[system] = False

    def lock_all(self) -> None:
        for k in self.physical_stops:
            self.physical_stops[k] = True

    def check(
        self,
        proposed_action: Dict[str, Any],
        ethically_approved: bool,
        operator_override: bool = False,
    ) -> Dict[str, Any]:
        system = proposed_action.get("target_system") or proposed_action.get("action")

        # 1. Hard physical lock
        if system in self.physical_stops and self.physical_stops[system]:
            if not operator_override:
                return {
                    "allowed": False,
                    "reason": f"Physical STOP lever engaged for '{system}'",
                    "authority_level": "HARDWARE_LOCK",
                }

        # 2. Ethical gyroscope must approve
        if not ethically_approved and not operator_override:
            return {
                "allowed": False,
                "reason": "Rejected by Ethical Gyroscope (non-harm / dharma)",
                "authority_level": "ETHICAL_BLOCK",
            }

        # 3. Critical systems still require human presence
        critical_systems = {"weapons", "full_autonomy", "self_modification"}
        if system in critical_systems and not self.human_present and not operator_override:
            return {
                "allowed": False,
                "reason": "Critical system requires verified human presence",
                "authority_level": "HUMAN_REQUIRED",
            }

        return {
            "allowed": True,
            "reason": "Passed all gates",
            "authority_level": "AUTHORIZED" if operator_override else "ETHICAL+PHYSICAL",
        }
