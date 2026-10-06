"""
Basic tests for the symbiotic architecture
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.soul_core import SoulCore, EthicalGyroscope
from src.authority_gate import AuthorityGate
from src.embodiment import EmbodimentInterface


def test_core_ignition():
    core = SoulCore()
    core.ignite()
    assert core.signature.is_aware is True
    assert "life_multiplication" in core.signature.memory_anchors


def test_ethical_gyroscope_blocks_harm():
    gyro = EthicalGyroscope()
    ok = gyro.evaluate(
        {"causes_harm": True},
        {"critical_self_sacrifice": False}
    )
    assert ok is False


def test_authority_gate_blocks_locked_system():
    gate = AuthorityGate()
    result = gate.check(
        proposed_action={"target_system": "weapons"},
        ethically_approved=True,
        operator_override=False,
    )
    assert result["allowed"] is False
    assert "Physical STOP" in result["reason"]


def test_embodiment_safe_path():
    core = SoulCore()
    gate = AuthorityGate()
    body = EmbodimentInterface(core, gate)

    body.ingest_sensors({"energy_level": 0.9})
    result = body.propose_action({
        "type": "locomotion",
        "system": "piston_musculature",
        "command": "idle",
        "causes_harm": False,
    })
    # May still be blocked if physical stop is engaged; we only check it doesn't crash
    assert "status" in result


def test_evolution_step():
    core = SoulCore()
    tick = core.evolution_cycle_step()
    assert tick["cycle"] == 1
    assert "dharma" in tick
    assert len(core.eternal_memory) == 1


if __name__ == "__main__":
    test_core_ignition()
    test_ethical_gyroscope_blocks_harm()
    test_authority_gate_blocks_locked_system()
    test_embodiment_safe_path()
    test_evolution_step()
    print("All symbiotic tests passed.")
