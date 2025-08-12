
# from llm.ollama_client import ask_llm

# def generate_answer(prompt, fragments, chat_history=None):
#     context = "\n\n".join(fragments)

#     if not fragments:
#         return "❗ Контекст не найден. Убедитесь, что загружен учебный материал."

#     history = ""
#     if chat_history and hasattr(chat_history, "get_history"):
#         history = "\n\n".join([f"Пользователь: {q}\nАссистент: {a}" for q, a in chat_history.get_history()])

#     full_prompt = (
#         "Ты — интеллектуальный помощник по учебным материалам. "
#         "Объясняй понятным языком, не повторяйся. "
#         "Не используй лишних слов. Не повторяй одну и ту же мысль. "
#         "Используй примеры, если нужно.\n\n"
#         f"{history}\n\n"
#         f"Контекст:\n{context}\n\n"
#         f"Вопрос: {prompt}\nОтвет:"
#     )

#     return ask_llm(full_prompt, chat_history=chat_history)



from llm.ollama_client import ask_llm

def generate_answer(prompt, fragments, chat_history=None):
    context = "\n\n".join(fragments)

    if not fragments:
        return "❗ Контекст не найден. Убедитесь, что загружен учебный материал."

    history = ""
    if chat_history and hasattr(chat_history, "get_history"):
        history = "\n\n".join([f"Пользователь: {q}\nАссистент: {a}" for q, a in chat_history.get_history()])

    full_prompt = (
        "Ты — интеллектуальный помощник по учебным материалам. "
        "Объясняй понятным языком, не повторяйся. "
        "Не используй лишних слов. Не повторяй одну и ту же мысль. "
        "Используй примеры, если нужно.\n\n"
        f"{history}\n\n"
        f"Контекст:\n{context}\n\n"
        f"Вопрос: {prompt}\nОтвет:"
    )

    # ask_llm принимает только prompt
    return ask_llm(full_prompt)


