# # import ollama
# # import os

# # def ask_llm(prompt: str) -> str:
# #     try:
# #         model = os.getenv("OLLAMA_MODEL", "llama3.1:latest")
# #         response = ollama.chat(
# #             model=model,
# #             messages=[
# #                 {'role': 'user', 'content': prompt}
# #             ]
# #         )
# #         return response.get("message", {}).get("content", "").strip() or "⚠️ Модель не вернула ответа."
    
# #     except Exception as e:
# #         return f"⚠️ Ошибка при вызове LLM: {e}"



# # llm/ollama_client.py
# import os
# import ollama
# from typing import Optional, List, Tuple, Union

# def _history_to_messages(chat_history: Optional[Union[object, List[dict], List[Tuple[str, str]]]]) -> List[dict]:
#     """
#     Поддерживает:
#       - объект с .get_history() -> List[Tuple[question, answer]]
#       - List[{"role": "...", "content": "..."}]
#       - List[Tuple[str, str]]  (q, a)
#       - None
#     Возвращает список сообщений формата Ollama.
#     """
#     if not chat_history:
#         return []

#     # Уже в формате сообщений?
#     if isinstance(chat_history, list) and chat_history and isinstance(chat_history[0], dict):
#         return chat_history  # [{"role":"user"/"assistant"/"system","content":"..."}]

#     msgs: List[dict] = []

#     # ConversationHistory(get_history -> [(q, a), ...])
#     if hasattr(chat_history, "get_history") and callable(chat_history.get_history):
#         try:
#             pairs = chat_history.get_history()
#         except Exception:
#             return []
#         for q, a in pairs:
#             if q:
#                 msgs.append({"role": "user", "content": q})
#             if a:
#                 msgs.append({"role": "assistant", "content": a})
#         return msgs

#     # Список пар (q, a)
#     if isinstance(chat_history, list) and chat_history and isinstance(chat_history[0], (list, tuple)) and len(chat_history[0]) == 2:
#         for q, a in chat_history:
#             if q:
#                 msgs.append({"role": "user", "content": q})
#             if a:
#                 msgs.append({"role": "assistant", "content": a})
#         return msgs

#     return []

# def ask_llm(prompt: str, chat_history: Optional[Union[object, List[dict], List[Tuple[str, str]]]] = None) -> str:
#     """
#     Отправляет запрос в Ollama, учитывая историю диалога (опционально).
#     """
#     try:
#         model = os.getenv("OLLAMA_MODEL", "llama3.1:latest")

#         system_msg = {
#             "role": "system",
#             "content": (
#                 "Ты — тьютор по учебным материалам. Отвечай кратко и по делу, "
#                 "опираясь на переданный контекст. Если контекста нет — скажи об этом."
#             )
#         }

#         messages: List[dict] = [system_msg]
#         messages.extend(_history_to_messages(chat_history))
#         messages.append({"role": "user", "content": prompt})

#         response = ollama.chat(model=model, messages=messages)
#         return response.get("message", {}).get("content", "").strip() or "⚠️ Модель не вернула ответа."
#     except Exception as e:
#         return f"⚠️ Ошибка при вызове LLM: {e}"



import ollama
import os

def ask_llm(prompt: str) -> str:
    try:
        # Используем Qwen по умолчанию

        # model = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b-instruct")
        model = "qwen2.5:1.5b-instruct"


        response = ollama.chat(
            model=model,
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        return response.get("message", {}).get("content", "").strip() or "⚠️ Модель не вернула ответа."
    
    except Exception as e:
        return f"⚠️ Ошибка при вызове LLM: {e}"
