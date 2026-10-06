"""
Embodiment Interface for Sovereign Soul Frame — Mark V
Abstract bridge between SoulCore and the mechanical steampunk substrate.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from .soul_core import SoulCore
from .authority_gate import AuthorityGate


class EmbodimentInterface:
    """
    Maps software decisions to mechanical systems of the Mark V frame
    and feeds sensor data back into the pneuma core.
    """

    def __init__(self, core: SoulCore, gate: AuthorityGate):
        self.core = core
        self.gate = gate
        self.sensor_buffer: Dict[str, float] = {}
        self.last_actuator_cmd: Dict[str, Any] = {}

    def ingest_sensors(self, sensor_data: Dict[str, float]) -> None:
        """Receive data from mechanical sensors (or simulation)."""
        self.sensor_buffer.update(sensor_data)

    def propose_action(self, intent: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full pipeline:
        1. Reflective cognition
        2. Ethical gyroscope
        3. Authority Gate (hardware + software STOP)
        4. Return safe command or rejection
        """
        # 1. Reflective step
        reflection = self.core.reflective_step(intent)

        # 2. Build proposed action for gyroscope
        proposed = {
            "action": intent.get("type", "unknown"),
            "causes_harm": intent.get("causes_harm", False),
            "saves_life_at_cost": intent.get("saves_life_at_cost", False),
            "target_system": intent.get("system"),
        }

        context = {
            "critical": intent.get("critical", False),
            "sensor_coherence": self._compute_coherence(),
        }

        # 3. Ethical evaluation
        ethically_ok = self.core.gyro.evaluate(proposed, context)

        # 4. Authority Gate (physical levers + software)
        final = self.gate.check(
            proposed_action=proposed,
            ethically_approved=ethically_ok,
            operator_override=intent.get("operator_override", False),
        )

        if final["allowed"]:
            self.last_actuator_cmd = {
                "system": intent.get("system"),
                "command": intent.get("command"),
                "params": intent.get("params", {}),
                "authority": final["authority_level"],
            }
            return {
                "status": "EXECUTE",
                "command": self.last_actuator_cmd,
                "reflection": reflection,
            }
        else:
            return {
                "status": "BLOCKED",
                "reason": final["reason"],
                "reflection": reflection,
            }

    def _compute_coherence(self) -> float:
        if not self.sensor_buffer:
            return 0.5
        values = list(self.sensor_buffer.values())
        return float(max(0.0, min(1.0, sum(values) / len(values))))

    def run_evolution_tick(self) -> Dict[str, Any]:
        """Advance the continuous evolution loop by one step."""
        return self.core.evolution_cycle_step()
