def should_hint(question: str) -> bool:
    return any(word in question.lower() for word in ["реши", "посчитай", "вычисли", "доказать", "найди"])

def generate_hint(question: str) -> str:
    return f"Интересный вопрос. А как ты думаешь, с чего можно начать решение задачи: '{question}'?"