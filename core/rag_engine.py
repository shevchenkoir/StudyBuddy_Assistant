# from vector_db.faiss_interface import search_similar_chunks
# from llm.answer_generator import generate_answer

# def get_answer(question):
#     relevant_chunks = search_similar_chunks(question)
#     return generate_answer(question, relevant_chunks)


# core/rag_engine.py
from llm.ollama_client import ask_llm

from llm.answer_generator import generate_answer
from vector_db.faiss_interface import search_similar_chunks

def get_answer(prompt, chat_history=None):
    relevant_chunks = search_similar_chunks(prompt)
    if not relevant_chunks:
        return "Не удалось найти ответ в учебных материалах. Попробуйте переформулировать вопрос или загрузите другой файл."

    return generate_answer(prompt, relevant_chunks, chat_history)
