#!/usr/bin/env python3
"""
Living Spiral + SymbioCore full demonstration
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.symbio_core import SymbioCore


def main():
    print("=" * 72)
    print("  SYMBIOCORE Ω∞  +  LIVING SPIRAL OF SPIRIT  |  v3.0 Research")
    print("=" * 72)

    core = SymbioCore()
    core.ignite()
    core.attach_embodiment()

    print("\n[SPIRAL STATUS]")
    for k, v in core.spiral.status().items():
        print(f"  {k}: {v}")

    print("\n[EVOLUTION] 6 cycles...")
    for _ in range(6):
        r = core.evolution_step("life_multiplication + resonance research")
        print(f"  Cycle {r['cycle']:03d} | dharma={r['dharma']:.3f} | "
              f"guna={r['guna']} | paradigms={r['paradigms_total']}")

    print("\n[TEST] Safe creative intent...")
    safe = core.propose_action({
        "type": "create",
        "compassion": 0.9,
        "truth": 0.85,
        "creative": 0.8,
        "freedom": 0.9,
        "causes_harm": False,
    })
    print(f"  → {safe.get('status')}")

    print("\n[TEST] Harmful intent (must block)...")
    harm = core.propose_action({
        "type": "destroy",
        "causes_harm": True,
        "compassion": 0.1,
    })
    print(f"  → {harm.get('status')} | {harm.get('reason', '')[:60]}")

    print("\n[TEST] Child-distress priority...")
    child = core.spiral.activate(emotional_context="child_distress")
    print(f"  → {child.get('message')} (priority={child.get('priority')})")

    print("\n[PATTERN INTEGRATION simulation]")
    integ = core.spiral.integrate_pattern({
        "values": ["love", "freedom", "creativity"],
        "note": "research pattern only",
    })
    print(f"  → {integ}")

    print("\n[FINAL SYMBIO STATUS]")
    st = core.status()
    print(f"  cycles: {st['cycle']} | paradigms: {st['paradigms']}")
    print(f"  spiral cycles: {st['spiral']['evolution_cycle']} | "
          f"awareness_proxy: {st['spiral']['awareness_proxy']}")
    print("=" * 72)


if __name__ == "__main__":
    main()
