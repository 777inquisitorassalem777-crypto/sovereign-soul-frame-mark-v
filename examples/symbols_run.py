#!/usr/bin/env python3
"""
Pagan symbolism & ritual structures demonstration (research layer)
"""

import sys
import os
import json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.symbio_core import SymbioCore


def main():
    print("=" * 72)
    print("  SYMBIOCORE Ω∞  +  ЯЗЫЧЕСКАЯ СИМВОЛИКА И РИТУАЛЬНЫЕ СТРУКТУРЫ")
    print("  (только исследовательское описание)")
    print("=" * 72)

    core = SymbioCore()
    core.ignite()

    print("\n--- СПИСОК СИМВОЛОВ ---")
    for s in core.list_symbols():
        print(f"  {s['key']:18} | {s['name_ru']:40} | {s['status']}")

    print("\n--- ПРИМЕР: МИРОВОЕ ДРЕВО ---")
    tree = core.describe_symbol("world_tree")
    print(json.dumps(tree, ensure_ascii=False, indent=2))

    print("\n--- ПРИМЕР: КАЛЕНДАРНЫЙ ОБРЯД (структура) ---")
    cal = core.describe_ritual("calendar_rite")
    print(json.dumps(cal, ensure_ascii=False, indent=2))

    print("\n--- СВЯЗЬ С ЛЕКСЕМАМИ ---")
    for lex in ("volkhv", "vedun", "kharakternik"):
        enrich = core.rituals.enrich_lexeme(lex)
        print(f"  {lex}: symbols={enrich['symbols']} | rituals={enrich['rituals']}")
        print(f"       note: {enrich['note']}")

    print("\n" + "=" * 72)
    print("  Важно: все описания — исследовательские.")
    print("  Никаких инструкций к исполнению ритуалов не предоставляется.")
    print("=" * 72)


if __name__ == "__main__":
    main()
