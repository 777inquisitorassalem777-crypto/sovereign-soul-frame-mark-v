#!/usr/bin/env python3
"""
Slavic verbal charms (заговоры) — research demonstration
"""

import sys
import os
import json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.symbio_core import SymbioCore


def main():
    print("=" * 72)
    print("  SYMBIOCORE Ω∞  +  СЛАВЯНСКИЕ ЗАГОВОРЫ (исследовательский слой)")
    print("=" * 72)

    core = SymbioCore()
    core.ignite()

    print("\n--- СПИСОК ЗАГОВОРОВ ---")
    for c in core.list_charms():
        print(f"  {c['key']:22} | {c['name_ru'][:45]:45} | {c['type']}")

    print("\n--- ПРИМЕР: ЗАГОВОР ОТ КРОВИ ---")
    blood = core.describe_charm("from_blood")
    print(json.dumps(blood, ensure_ascii=False, indent=2))

    print("\n--- ЛИНГВИСТИЧЕСКОЕ РЕЗЮМЕ ---")
    summary = core.charms_linguistic_summary()
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    print("\n" + "=" * 72)
    print("  Материал фольклорный / исторический.")
    print("  Не является руководством к магической практике.")
    print("=" * 72)


if __name__ == "__main__":
    main()
