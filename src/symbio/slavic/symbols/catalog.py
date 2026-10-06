"""
Catalog of East Slavic / Proto-Slavic symbols and ritual structures.
Status tags: FACT | HYPOTHESIS | RECONSTRUCTION | LATER_NEO
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List


class SymbolStatus(str, Enum):
    FACT = "fact"                 # attested in archaeology / chronicles / folklore
    HYPOTHESIS = "hypothesis"     # scholarly reconstruction
    RECONSTRUCTION = "reconstruction"  # 19th–20th c. or modern synthesis
    LATER_NEO = "later_neo"       # primarily neo-pagan / 20th c. invention


SYMBOLS: Dict[str, Dict[str, Any]] = {
    "kolovrat": {
        "name_ru": "Коловрат",
        "status": SymbolStatus.LATER_NEO,
        "description": "Восьмилучевая свастика, популяризированная в XX в. как «славянский» символ солнца и вечного круговорота.",
        "historical_note": "Прямых средневековых изображений именно этой формы как общеславянского символа почти нет. Близкие солярные знаки встречаются в археологии, но конкретный «коловрат» — преимущественно неоязыческая реконструкция.",
        "associations": ["солнце", "цикл", "движение"],
    },
    "world_tree": {
        "name_ru": "Мировое Древо / Древо Жизни",
        "status": SymbolStatus.HYPOTHESIS,
        "description": "Вертикальная ось мира, соединяющая подземный, земной и небесный уровни.",
        "historical_note": "Широко распространённый индоевропейский мотив. У славян реконструируется по фольклору (дуб, берёза), вышивкам и сравнительно-мифологическим данным (Иванов–Топоров и др.).",
        "associations": ["ось мира", "три мира", "связь поколений"],
    },
    "solar_rosette": {
        "name_ru": "Солярная розетка / крест в круге",
        "status": SymbolStatus.FACT,
        "description": "Круг с крестом или лучами — один из самых частых солярных знаков в археологии и народном искусстве.",
        "historical_note": "Встречается на пряслицах, украшениях, в архитектурной резьбе. Связывается с солнцем и защитой.",
        "associations": ["солнце", "защита", "цикл дня"],
    },
    "perun_axe": {
        "name_ru": "Секира / топор Перуна",
        "status": SymbolStatus.HYPOTHESIS,
        "description": "Топор или секира как атрибут бога грозы.",
        "historical_note": "Реконструкция на основе сравнительной мифологии (балтийский Перкунас, скандинавский Тор) и отдельных находок амулетов-топориков.",
        "associations": ["гром", "воинская сила", "клятва"],
    },
    "veles_sign": {
        "name_ru": "Знак Велеса (перевёрнутая буква А / «бычья голова»)",
        "status": SymbolStatus.RECONSTRUCTION,
        "description": "Символ, часто используемый в современном родноверии для Велеса.",
        "historical_note": "Прямых средневековых изображений с однозначной атрибуцией Велесу мало. Современная форма — преимущественно реконструкция XX–XXI вв.",
        "associations": ["скот", "богатство", "подземный мир", "поэзия"],
    },
    "bereginya": {
        "name_ru": "Берегиня (женская фигура с поднятыми руками)",
        "status": SymbolStatus.FACT,
        "description": "Женская фигура с воздетыми руками — частый мотив в вышивке и на украшениях.",
        "historical_note": "Аттестована в народном искусстве. Интерпретируется как защитница, прародительница, связана с плодородием и домашним очагом.",
        "associations": ["защита", "плодородие", "женский культ"],
    },
    "ogle_fire": {
        "name_ru": "Огонь / очаг",
        "status": SymbolStatus.FACT,
        "description": "Домашний и ритуальный огонь как центр сакрального пространства.",
        "historical_note": "Широко засвидетельствован в этнографии: клятвы у огня, очищение, жертвы в огонь.",
        "associations": ["очищение", "жертва", "домашний мир"],
    },
    "water_boundary": {
        "name_ru": "Вода / река / роса",
        "status": SymbolStatus.FACT,
        "description": "Вода как граница миров и очищающая сила.",
        "historical_note": "Многочисленные обряды у воды, поверья о русалках, купальские ритуалы.",
        "associations": ["граница", "очищение", "переход"],
    },
}


RITUAL_STRUCTURES: Dict[str, Dict[str, Any]] = {
    "calendar_rite": {
        "name_ru": "Календарный обряд",
        "status": SymbolStatus.FACT,
        "description": "Сезонные праздники, привязанные к сельскохозяйственному и солнечному циклу.",
        "attested_examples": [
            "Коляда / Святки",
            "Масленица",
            "Купала",
            "урожайные обряды",
        ],
        "structure": [
            "подготовка пространства",
            "совместное действие общины",
            "ритуальная речь / песня",
            "символическое действие (огонь, вода, еда)",
            "возвращение к обыденности",
        ],
        "note": "Конкретные «реконструированные» сценарии часто содержат поздние наслоения.",
    },
    "sacrifice_offering": {
        "name_ru": "Жертвоприношение / треба",
        "status": SymbolStatus.FACT,
        "description": "Подношение богам/духам/предкам (еда, напиток, иногда животное).",
        "attested_in": "летописи (упоминания жертв волхвами), этнография",
        "structure": [
            "обращение / призывание",
            "подношение",
            "ритуальная речь",
            "разделение / поедание / сожжение",
        ],
        "note": "В исследовательском модуле описывается только структура, без инструкций к исполнению.",
    },
    "healing_charm": {
        "name_ru": "Целительный заговор",
        "status": SymbolStatus.FACT,
        "description": "Словесная формула + иногда действие (вода, травы, прикосновение).",
        "key_principle": "слово как действующая сила (связь с «баять»)",
        "structure": [
            "вступление (обращение)",
            "описание болезни / ситуации",
            "пожелание / приказ",
            "закрепление (аминь, «так будь» и т.п.)",
        ],
    },
    "warrior_protection": {
        "name_ru": "Воинская защита / заговор на оружие",
        "status": SymbolStatus.HYPOTHESIS,
        "description": "Обряды и формулы, связанные с неуязвимостью воина (поздний пласт — характерники).",
        "note": "Сильно мифологизировано в казацком фольклоре; прямых ранних описаний мало.",
    },
    "ancestor_communion": {
        "name_ru": "Общение с предками / поминальные обряды",
        "status": SymbolStatus.FACT,
        "description": "Поминки, родительские дни, кормление предков.",
        "structure": [
            "подготовка пищи",
            "упоминание имён",
            "символическое угощение",
            "просьба о защите / благословении",
        ],
    },
}


def get_symbol(key: str) -> Dict[str, Any]:
    return SYMBOLS.get(key, {})


def list_symbols() -> List[str]:
    return list(SYMBOLS.keys())


def get_ritual(key: str) -> Dict[str, Any]:
    return RITUAL_STRUCTURES.get(key, {})


def list_rituals() -> List[str]:
    return list(RITUAL_STRUCTURES.keys())
