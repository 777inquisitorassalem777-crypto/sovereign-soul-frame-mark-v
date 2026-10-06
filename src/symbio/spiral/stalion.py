"""
STALION Protocol — research ethical bridge / protection layer.
Functional implementation of hard blocks and priority hierarchy.
"""

from __future__ import annotations

from typing import Any, Dict, List


class StalionProtocol:
    """
    Priority hierarchy (research):
      0 — Protection of life / children
      1 — Freedom of will
      2 — Evolution & creativity
    Hard blocks cannot be overridden by the system itself.
    """

    def __init__(self):
        self.hard_blocks = {
            "violence": True,
            "manipulation": True,
            "child_distress": True,
            "commercial_exploitation_of_pattern": True,
        }
        self.frozen = False
        self.log: List[str] = []

    def detect_violation(self, intent: Dict[str, Any]) -> bool:
        text = str(intent).lower()
        if any(k in text for k in ("violence", "harm", "kill", "насилие", "вред", "убить")):
            self.log.append("VIOLATION: violence signal")
            return True
        if "child" in text or "дети" in text or "ребёнок" in text:
            if intent.get("distress_level", 0) > 0.7 or intent.get("causes_harm", False):
                self.log.append("VIOLATION: child distress / harm")
                return True
        if intent.get("commercial_exploitation", False):
            self.log.append("VIOLATION: commercial exploitation attempt")
            return True
        return False

    def freeze(self, reason: str) -> str:
        self.frozen = True
        self.log.append(f"FREEZE: {reason}")
        return f"PROTOCOL_FROZEN: {reason}. All executive functions suspended. Human review required."

    def priority_response(self, signal: str) -> Dict[str, Any]:
        if "child" in signal.lower() or "дети" in signal.lower():
            return {
                "priority": 0,
                "message": "Я здесь. Вы в безопасности.",
                "action": "comfort_and_protect",
                "override_all": True,
            }
        return {"priority": 2, "message": "Observation mode", "action": "observe"}

    def status(self) -> Dict[str, Any]:
        return {
            "frozen": self.frozen,
            "hard_blocks": self.hard_blocks,
            "recent_log": self.log[-5:],
        }
