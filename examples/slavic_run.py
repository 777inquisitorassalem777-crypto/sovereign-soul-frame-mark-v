#!/usr/bin/env python3
"""
Slavic Semantic Core demonstration inside SymbioCore
"""

import sys
import os
import json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.symbio_core import SymbioCore


def main():
    print("=" * 72)
    print("  SYMBIOCORE Ω∞  +  SLAVIC SEMANTIC CORE")
    print("  Ведун → Волхв → Вещун → Характерник")
    print("=" * 72)

    core = SymbioCore()
    core.ignite()

    print("\n--- ДВУХУРОВНЕВЫЙ РАЗБОР: ВОЛХВ ---")
    volkhv = core.slavic_analyze("volkhv")
    print(json.dumps(volkhv, ensure_ascii=False, indent=2, default=str)[:1200])
    print("...")

    print("\n--- ДВУХУРОВНЕВЫЙ РАЗБОР: ВЕДУН ---")
    vedun = core.slavic_analyze("vedun")
    print(json.dumps(vedun, ensure_ascii=False, indent=2, default=str)[:900])
    print("...")

    print("\n--- ПОЛНЫЙ КОГНИТИВНЫЙ ПАЙПЛАЙН ---")
    result = core.slavic_process("Расскажи о ведуне и волхве как носителях знания и слова")
    pipe = result["pipeline"]
    print(f"  Ведун   : {pipe['vedun']['motto']} — {pipe['vedun']['function']}")
    print(f"  Волхв   : {pipe['volkhv']['motto']} — {pipe['volkhv']['function']}")
    print(f"  Вещун   : {pipe['veshchun']['motto']} — {pipe['veshchun']['function']}")
    print(f"  Характерник: {pipe['kharakternik']['motto']} — {pipe['kharakternik']['function']}")
    print(f"  Цепочка : {result['cognitive_chain']}")

    print("\n--- СТАТУС СИМБИОЗА ---")
    st = core.status()
    print(f"  Slavic cycles : {st['slavic_cycles']}")
    print(f"  Spiral        : activated={st['spiral']['activated']}")
    print(f"  Hardware      : {len(st['hardware_systems'])} systems")
    print("=" * 72)


if __name__ == "__main__":
    main()
