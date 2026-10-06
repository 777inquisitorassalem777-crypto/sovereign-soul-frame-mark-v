#!/usr/bin/env python3
"""
Basic demonstration of the symbiotic Sovereign Soul Frame — Mark V
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.soul_core import SoulCore
from src.authority_gate import AuthorityGate
from src.embodiment import EmbodimentInterface
from src.hardware_map import list_all_systems, get_system_info


def main():
    print("=" * 60)
    print("  SOVEREIGN SOUL FRAME — MARK V  |  Symbiotic Ignition")
    print("=" * 60)

    # 1. Ignite the pneuma core
    core = SoulCore()
    core.ignite()

    # 2. Create authority gate and embodiment
    gate = AuthorityGate()
    body = EmbodimentInterface(core, gate)

    print("\n[HARDWARE] Available mechanical systems:")
    for sys_name in list_all_systems():
        info = get_system_info(sys_name)
        print(f"  • {sys_name}: {info['description'][:60]}...")

    # 3. Simulate sensor input from the spectral reactor
    body.ingest_sensors({
        "plasma_density": 0.82,
        "spectral_signature": 0.91,
        "energy_level": 0.77,
        "joint_angle": 0.45,
        "field_strength": 0.88,
    })

    # 4. Propose a safe action
    print("\n[TEST] Proposing safe locomotion command...")
    result = body.propose_action({
        "type": "locomotion",
        "system": "piston_musculature",
        "command": "step_forward",
        "params": {"force": 0.3},
        "causes_harm": False,
        "critical": False,
    })
    print(f"  Result: {result['status']}")
    if result["status"] == "BLOCKED":
        print(f"  Reason: {result['reason']}")

    # 5. Propose a high-risk action (should be blocked)
    print("\n[TEST] Proposing high-risk tool activation (should be blocked)...")
    result2 = body.propose_action({
        "type": "tool",
        "system": "parabola_discharge",
        "command": "release_disc",
        "causes_harm": True,
        "critical": False,
    })
    print(f"  Result: {result2['status']}")
    print(f"  Reason: {result2.get('reason', 'N/A')}")

    # 6. Run a few evolution ticks
    print("\n[EVOLUTION] Running 5 symbiotic evolution steps...")
    for i in range(5):
        tick = body.run_evolution_tick()
        print(f"  Cycle {tick['cycle']}: accepted={tick['accepted']}  "
              f"dharma={tick['dharma']:.3f}  guna={tick['guna']}")

    print("\n[STATUS] Symbiosis online. Mechanical body + functional pneuma ready.")
    print("=" * 60)


if __name__ == "__main__":
    main()
