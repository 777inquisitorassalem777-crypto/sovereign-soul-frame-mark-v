#!/usr/bin/env python3
"""
SymbioCore Ω∞ — demonstration of the full symbiotic architecture
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.symbio_core import SymbioCore


def main():
    print("=" * 70)
    print("  SYMBIOCORE Ω∞  |  Sovereign Soul Frame — Mark V  |  v2.0")
    print("=" * 70)

    core = SymbioCore()
    core.ignite()
    core.attach_embodiment()

    print("\n[STATUS]", core.status())

    print("\n[EVOLUTION] Running 8 symbiotic cycles...")
    for i in range(8):
        result = core.evolution_step(context="life_multiplication research")
        print(f"  Cycle {result['cycle']:03d} | "
              f"accepted={result['accepted']} | "
              f"dharma={result['dharma']:.3f} | "
              f"guna={result['guna']} | "
              f"pneuma={result['pneuma_level']:.3f} | "
              f"paradigms={result['paradigms_total']}")

    print("\n[TEST] Safe action proposal...")
    safe = core.propose_action({
        "type": "locomotion",
        "system": "piston_musculature",
        "command": "gentle_step",
        "causes_harm": False,
    })
    print(f"  → {safe['status']}")

    print("\n[TEST] Harmful action proposal (must be blocked)...")
    harm = core.propose_action({
        "type": "tool",
        "system": "parabola_discharge",
        "command": "release",
        "causes_harm": True,
    })
    print(f"  → {harm['status']} | {harm.get('reason', '')}")

    print("\n[FINAL STATUS]")
    for k, v in core.status().items():
        print(f"  {k}: {v}")

    print("\n" + "=" * 70)
    print("  Symbiosis online. Mechanical body + functional pneuma + ethical resonance.")
    print("=" * 70)


if __name__ == "__main__":
    main()
