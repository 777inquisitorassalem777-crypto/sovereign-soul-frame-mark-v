"""
Historical-linguistic seed data for key Slavic sacred-knowledge terms.
Strict separation: FACT / HYPOTHESIS / INTERPRETATION / DISPUTED.
"""

from __future__ import annotations

from enum import Enum
from typing import Dict, Any, List


class LexemeStatus(str, Enum):
    FACT = "fact"                 # well-attested in sources
    HYPOTHESIS = "hypothesis"     # plausible scholarly reconstruction
    INTERPRETATION = "interpretation"  # modern semantic/philosophical reading
    DISPUTED = "disputed"         # competing etymologies or folk etymology


LEXEMES: Dict[str, Dict[str, Any]] = {
    "volkhv": {
        "forms": {
            "old_russian": "вълхвъ",
            "old_church_slavonic": "влъхвъ",
            "proto_slavic": "*vъlxvъ / *vьlxvъ",
        },
        "etymology": {
            "primary": {
                "status": LexemeStatus.FACT,
                "link": "ст.-слав. влъснѫти ‘говорить невнятно, бормотать’",
                "derived": ["влъшьба → волшебство", "волхование"],
                "sources": ["Фасмер", "Трубачёв", "Аникин"],
            },
            "folk_etymology_wolf": {
                "status": LexemeStatus.DISPUTED,
                "note": "Связь с *vьlkъ ‘волк’ отвергается академической этимологией",
            },
            "veles_link": {
                "status": LexemeStatus.HYPOTHESIS,
                "note": "Гипотетическая связь с Велесом/Волосом остаётся спорной",
            },
        },
        "semantic_core": {
            "status": LexemeStatus.INTERPRETATION,
            "formula": "особая речь → тайное знание → ритуальное воздействие",
            "functions": [
                "жрец-прорицатель",
                "хранитель сакрального слова",
                "посредник Явь ↔ Навь/Правь",
                "календарные обряды и жертвы",
            ],
            "key_tool": "слово (заговор, бормотание, ритуальная речь)",
        },
        "period": "early (attested in Old Russian chronicles)",
    },
    "vedun": {
        "forms": {
            "old_russian": "вѣдунъ",
            "proto_slavic": "*vědunъ",
            "from_verb": "*věděti / ведать",
        },
        "etymology": {
            "primary": {
                "status": LexemeStatus.FACT,
                "ie_root": "*weid- / *wid- (‘видеть → знать’)",
                "cognates": [
                    "др.-инд. veda / vidyā",
                    "лат. vidēre",
                    "греч. οἶδα",
                    "гот. wait",
                ],
                "sources": ["Фасмер", "comparative IE dictionaries"],
            },
        },
        "semantic_core": {
            "status": LexemeStatus.INTERPRETATION,
            "formula": "видеть → распознать → знать → ведать",
            "functions": [
                "обладатель сокровенного знания",
                "знахарь / провидец",
                "знание трав, судеб, скрытых причин",
            ],
            "key_tool": "ведение (знание как сила)",
            "note": "Изначально нейтральный ‘знающий’; позже мог получать негативную коннотацию",
        },
        "period": "early (transparent IE formation)",
    },
    "veshchun": {
        "forms": {
            "related": ["вещий", "вещать", "вещун"],
        },
        "etymology": {
            "primary": {
                "status": LexemeStatus.FACT,
                "link": "вещать / вещий — сообщать о скрытом/будущем",
            },
        },
        "semantic_core": {
            "status": LexemeStatus.INTERPRETATION,
            "formula": "знать → предвидеть → возвещать",
            "functions": ["предсказатель", "возвеститель скрытого"],
            "key_tool": "речь-пророчество",
        },
        "period": "early–medieval",
    },
    "kharakternik": {
        "forms": {
            "ukrainian": "характерник",
            "attested": "XVI–XVIII вв., запорожская среда",
        },
        "etymology": {
            "primary": {
                "status": LexemeStatus.FACT,
                "source": "греч. χαρακτήρ ‘печать, отличительная черта’ → через польск./церк.-слав.",
                "note": "Не праславянское слово",
            },
            "folk_etymology": {
                "status": LexemeStatus.DISPUTED,
                "note": "Попытки вывести из ‘Хара + Ра’ научно не обоснованы",
            },
        },
        "semantic_core": {
            "status": LexemeStatus.INTERPRETATION,
            "formula": "особый внутренний ‘характер’ → сверхъестественная воинская способность",
            "functions": [
                "казак-воин с приписываемой неуязвимостью",
                "заговаривание ран и пуль",
                "невидимость, ‘заморочение’",
                "синкретизм народной магии + воинской этики",
            ],
            "key_tool": "внутренняя сила / воля / ‘печать’",
        },
        "period": "late (Cossack folklore)",
    },
    "znahar": {
        "forms": {"russian": "знахарь"},
        "semantic_core": {
            "status": LexemeStatus.INTERPRETATION,
            "formula": "знать → знать средство → уметь применять",
            "functions": ["практическое лечение", "народная медицина"],
            "key_tool": "прикладное знание",
        },
    },
    "baya": {
        "forms": {"related": ["баять", "баяльник", "заговор"]},
        "semantic_core": {
            "status": LexemeStatus.INTERPRETATION,
            "formula": "слово → воздействие",
            "functions": ["заговор", "заклинание", "ритуальная речь"],
            "key_tool": "действенное слово",
            "note": "В архаической модели правильно произнесённое слово участвует в изменении реальности",
        },
    },
}


def get_lexeme(key: str) -> Dict[str, Any]:
    return LEXEMES.get(key, {})


def list_lexemes() -> List[str]:
    return list(LEXEMES.keys())
