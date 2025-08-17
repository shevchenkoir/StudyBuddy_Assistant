# core/router.py
from typing import Dict, Tuple, Optional

DEFAULT_COURSES: Dict[str, Dict] = {
    "math": {
        "title": "Матанализ",
        "keywords": ["интеграл", "производная", "предел", "ряд", "матрица", "теорема", "уравнение", "градиент"],
    },
    "physics": {
        "title": "Физика",
        "keywords": ["механика", "оптика", "электричество", "индукция", "сила", "ускорение", "энергия", "напряжение"],
    },
}


def keyword_route(question: str, courses: Dict[str, Dict] = DEFAULT_COURSES) -> Tuple[str, float]:
    q = (question or "").lower()
    best_id, best_score = "general", 0
    for cid, cfg in courses.items():
        score = sum(1 for kw in cfg["keywords"] if kw in q)
        if score > best_score:
            best_id, best_score = cid, score
    confidence = min(1.0, best_score / 3.0)
    return best_id, confidence


def route_course(question: str) -> str:
    cid, conf = keyword_route(question)
    return cid
