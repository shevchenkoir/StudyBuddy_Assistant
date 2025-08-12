# from llm.ollama_client import ask_llm

# def generate_quiz(topic: str, n: int = 5):
#     prompt = f"Сгенерируй {n} простых вопросов по теме '{topic}' для самопроверки."
#     response = ask_llm(prompt)
#     return response

from llm.ollama_client import ask_llm

def generate_quiz(topic: str, n: int = 5):
    prompt = f"Сгенерируй {n} простых вопросов по теме '{topic}' для самопроверки."
    return ask_llm(prompt)
