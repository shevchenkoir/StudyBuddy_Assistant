

# # # # import sys, os
# # # # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# # # # import streamlit as st
# # # # from core.rag_engine import get_answer
# # # # from data_ingestion.pdf_loader import extract_text_from_pdf
# # # # from data_ingestion.docx_loader import extract_text_from_docx
# # # # from data_ingestion.preprocessor import clean_text
# # # # from data_ingestion.splitter import split_text
# # # # from vector_db.embedding_model import documents
# # # # from vector_db.faiss_interface import initialize_index


# # # # UPLOAD_DIR = "uploaded_materials"

# # # # def run_app():
# # # #     st.set_page_config(page_title="StudyBuddy", layout="wide")
# # # #     st.title("📘 StudyBuddy: Твой ИИ-тьютор")

# # # #     # Инициализация истории
# # # #     if "chat_history" not in st.session_state:
# # # #         st.session_state.chat_history = []

# # # #     # Загрузка и обработка файла
# # # #     uploaded_file = st.file_uploader("📚 Загрузите учебный материал (PDF или DOCX)", type=["pdf", "docx"])
# # # #     if uploaded_file:
# # # #         os.makedirs(UPLOAD_DIR, exist_ok=True)
# # # #         file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
# # # #         with open(file_path, "wb") as f:
# # # #             f.write(uploaded_file.getbuffer())
# # # #         st.success(f"Файл '{uploaded_file.name}' успешно загружен!")

# # # #         # Извлечение и индексирование текста
# # # #         if uploaded_file.name.endswith(".pdf"):
# # # #             raw_text = extract_text_from_pdf(file_path)
# # # #         else:
# # # #             raw_text = extract_text_from_docx(file_path)

# # # #         cleaned = clean_text(raw_text)
# # # #         chunks = split_text(cleaned)
# # # #         documents.clear()
# # # #         documents.extend(chunks)
# # # #         initialize_index()
# # # #         st.success("Материал проиндексирован и готов к использованию!")

# # # #     # Ввод вопроса
# # # #     st.subheader("💬 Введите вопрос")
# # # #     question = st.text_input("Ваш вопрос:")

# # # #     if st.button("Отправить") and question:
# # # #         st.session_state.chat_history.append({"role": "user", "content": question})
# # # #         answer = get_answer(question, st.session_state.chat_history)
# # # #         st.session_state.chat_history.append({"role": "assistant", "content": answer})
# # # #         st.markdown(f"**Ответ:** {answer}")

# # # #     # История
# # # #     if st.session_state.chat_history:
# # # #         with st.expander("📜 История диалога"):
# # # #             for entry in st.session_state.chat_history:
# # # #                 role = "🧑" if entry["role"] == "user" else "🤖"
# # # #                 st.markdown(f"{role} **{entry['role']}**: {entry['content']}")

# # # # # Запуск
# # # # if __name__ == "__main__":
# # # #     run_app()

# # # # from pathlib import Path
# # # # import sys, os
# # # # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# # # # import streamlit as st
# # # # from core.rag_engine import get_answer
# # # # from core.pedagogy import should_hint, generate_hint
# # # # from gui.session_manager import get_session_history
# # # # from llm.quiz_generator import generate_quiz
# # # # from ethics.user_feedback import save_feedback

# # # # from data_ingestion.pdf_loader import extract_text_from_pdf
# # # # from data_ingestion.docx_loader import extract_text_from_docx
# # # # from data_ingestion.splitter import split_text
# # # # from data_ingestion.preprocessor import clean_text
# # # # from vector_db.embedding_model import documents
# # # # from vector_db.faiss_interface import initialize_index

# # # # from vector_db.embedding_model import documents, create_embeddings
# # # # from vector_db.faiss_interface import initialize_index

# # # # UPLOAD_DIR = "uploaded_materials"

# # # # def handle_file_upload():
# # # #     st.subheader("📚 Загрузка учебного материала")
# # # #     uploaded_file = st.file_uploader("Выберите PDF или DOCX файл", type=["pdf", "docx"])
# # # #     if uploaded_file:
# # # #         os.makedirs(UPLOAD_DIR, exist_ok=True)
# # # #         file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
# # # #         with open(file_path, "wb") as f:
# # # #             f.write(uploaded_file.getbuffer())
# # # #         st.success(f"Файл '{uploaded_file.name}' загружен успешно!")

# # # #         try:
# # # #             # 📖 Извлечение текста
# # # #             if uploaded_file.name.endswith(".pdf"):
# # # #                 raw_text = extract_text_from_pdf(file_path)
# # # #             else:
# # # #                 raw_text = extract_text_from_docx(file_path)

# # # #             # 🧹 Очистка и разбиение
# # # #             cleaned = clean_text(raw_text)
# # # #             chunks = split_text(cleaned)
# # # #             documents.clear()
# # # #             documents.extend(chunks)

# # # #             # 🧠 Генерация эмбеддингов + инициализация поиска
# # # #             create_embeddings(documents)
# # # #             initialize_index()

# # # #             st.success("Материал проиндексирован и готов к использованию!")
# # # #         except Exception as e:
# # # #             st.error(f"Ошибка при обработке файла: {e}")


# # # # def run_app():
# # # #     st.set_page_config(page_title="StudyBuddy", layout="wide")
# # # #     st.title("📘 StudyBuddy: Интеллектуальный помощник")

# # # #     handle_file_upload()

# # # #     history = get_session_history()
# # # #     tab1, tab2 = st.tabs(["💬 Задать вопрос", "📝 Quiz"])

# # # #     with tab1:
# # # #         st.subheader("Диалог с ассистентом")
# # # #         question = st.text_input("Введите вопрос:")
# # # #         use_pedagogy = st.checkbox("Режим подсказок (не давать решение)", value=True)

# # # #         if st.button("Ответить") and question:
# # # #             if use_pedagogy and should_hint(question):
# # # #                 answer = generate_hint(question)
# # # #             else:
# # # #                 answer = get_answer(question, st.session_state.chat_history)

# # # #             history.add_turn(question, answer)
# # # #             st.markdown(f"**Ответ:** {answer}")

# # # #             st.markdown("---")
# # # #             st.markdown("Оцените ответ:")
# # # #             col1, col2 = st.columns(2)
# # # #             with col1:
# # # #                 if st.button("👍 Полезно"):
# # # #                     save_feedback(question, answer, True)
# # # #             with col2:
# # # #                 if st.button("👎 Не полезно"):
# # # #                     save_feedback(question, answer, False)

# # # #         st.markdown("### История диалога:")
# # # #         for q, a in history.get_history():
# # # #             st.markdown(f"**Вы:** {q}\\n\\n**Бот:** {a}")

# # # #     with tab2:
# # # #         st.subheader("Генерация теста по теме")
# # # #         topic = st.text_input("Введите тему для теста:")
# # # #         num_q = st.slider("Количество вопросов", 1, 10, 5)

# # # #         if st.button("Создать Quiz"):
# # # #             quiz = generate_quiz(topic, num_q)
# # # #             st.text_area("Вопросы для самопроверки", quiz, height=300)

# # # # if __name__ == "__main__":
# # # #     run_app()

# # # # import sys, os
# # # # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# # # # from config import embedding_model, OLLAMA_MODEL

# # # import sys, os
# # # from pathlib import Path
# # # sys.path.append(str(Path(__file__).parent.parent))
# # # from config import embedding_model, OLLAMA_MODEL

# # # # Принудительно задаём модель Qwen
# # # import os as _os

# # # _os.environ.setdefault("OLLAMA_MODEL", "qwen2.5:1.5b-instruct")  # для ответов
# # # _os.environ.setdefault("OLLAMA_EMBED_MODEL", "nomic-embed-text") # для эмбеддингов
# # # _os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")



# # # import streamlit as st
# # # from core.rag_engine import get_answer
# # # from core.pedagogy import should_hint, generate_hint
# # # from gui.session_manager import get_session_history
# # # from llm.quiz_generator import generate_quiz
# # # from ethics.user_feedback import save_feedback

# # # from data_ingestion.pdf_loader import extract_text_from_pdf
# # # from data_ingestion.docx_loader import extract_text_from_docx
# # # from data_ingestion.splitter import split_text
# # # from data_ingestion.preprocessor import clean_text
# # # from vector_db.faiss_interface import initialize_index

# # # UPLOAD_DIR = "uploaded_materials"




# # # import sys, os
# # # from pathlib import Path
# # # sys.path.append(str(Path(__file__).parent.parent))
# # # from config import OLLAMA_MODEL, embedding_model


# # # import streamlit as st
# # # from core.rag_engine import get_answer
# # # from core.pedagogy import should_hint, generate_hint
# # # from gui.session_manager import get_session_history
# # # from llm.quiz_generator import generate_quiz
# # # from ethics.user_feedback import save_feedback

# # # from data_ingestion.pdf_loader import extract_text_from_pdf
# # # from data_ingestion.docx_loader import extract_text_from_docx
# # # from data_ingestion.splitter import split_text
# # # from data_ingestion.preprocessor import clean_text
# # # from vector_db.faiss_interface import initialize_index

# # # UPLOAD_DIR = "uploaded_materials"

# # # def handle_file_upload():
# # #     st.subheader("📚 Загрузка учебного материала")
# # #     uploaded_file = st.file_uploader("Выберите PDF или DOCX файл", type=["pdf", "docx"])
# # #     if uploaded_file:
# # #         os.makedirs(UPLOAD_DIR, exist_ok=True)
# # #         file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
# # #         with open(file_path, "wb") as f:
# # #             f.write(uploaded_file.getbuffer())
# # #         st.success(f"Файл '{uploaded_file.name}' загружен успешно!")

# # #         try:
# # #             st.write("📄 Извлечение текста из файла...")
# # #             if uploaded_file.name.endswith(".pdf"):
# # #                 raw_text = extract_text_from_pdf(file_path)
# # #             else:
# # #                 raw_text = extract_text_from_docx(file_path)

# # #             st.write(f"📜 Извлечено {len(raw_text)} символов текста.")

# # #             cleaned = clean_text(raw_text)
# # #             st.write(f"🧹 После очистки: {len(cleaned)} символов.")

# # #             chunks = split_text(cleaned)
# # #             st.write(f"🔹 Чанков создано: {len(chunks)}")
# # #             if chunks:
# # #                 st.write(f"🧩 Пример чанка:\n\n{chunks[0]}")

# # #             st.write("🔍 Инициализация индекса...")
# # #             initialize_index(chunks)

# # #             st.session_state["documents"] = chunks
# # #             st.success("Материал проиндексирован и готов к использованию!")
# # #         except Exception as e:
# # #             st.error(f"❌ Ошибка при обработке файла: {e}")

# # # def run_app():
# # #     st.set_page_config(page_title="StudyBuddy", layout="wide")
# # #     st.title("📘 StudyBuddy: Интеллектуальный помощник")

# # #     handle_file_upload()

# # #     history = get_session_history()
# # #     tab1, tab2 = st.tabs(["💬 Задать вопрос", "📝 Quiz"])

# # #     with tab1:
# # #         st.subheader("Диалог с ассистентом")
# # #         question = st.text_input("Введите вопрос:")
# # #         use_pedagogy = st.checkbox("Режим подсказок (не давать решение)", value=True)

# # #         if st.button("Ответить") and question:
# # #             if "documents" not in st.session_state or not st.session_state["documents"]:
# # #                 st.warning("❗ Сначала загрузите и проиндексируйте учебный материал.")
# # #             else:
# # #                 if use_pedagogy and should_hint(question):
# # #                     answer = generate_hint(question)
# # #                 else:
# # #                     answer = get_answer(question, st.session_state.chat_history)

# # #                 history.add_turn(question, answer)
# # #                 st.markdown(f"**Ответ:** {answer}")

# # #                 st.markdown("---")
# # #                 st.markdown("Оцените ответ:")
# # #                 col1, col2 = st.columns(2)
# # #                 with col1:
# # #                     if st.button("👍 Полезно"):
# # #                         save_feedback(question, answer, True)
# # #                 with col2:
# # #                     if st.button("👎 Не полезно"):
# # #                         save_feedback(question, answer, False)

# # #         st.markdown("### История диалога:")
# # #         for q, a in history.get_history():
# # #             st.markdown(f"**Вы:** {q}\n\n**Бот:** {a}")

# # #     with tab2:
# # #         st.subheader("Генерация теста по теме")
# # #         topic = st.text_input("Введите тему для теста:")
# # #         num_q = st.slider("Количество вопросов", 1, 10, 5)

# # #         if st.button("Создать Quiz"):
# # #             quiz = generate_quiz(topic, num_q)
# # #             st.text_area("Вопросы для самопроверки", quiz, height=300)

# # # if __name__ == "__main__":
# # #     run_app()
# import sys, os
# from pathlib import Path
# sys.path.append(str(Path(__file__).parent.parent))
# from config import embedding_model, OLLAMA_MODEL
# from output.speech_output import speak

# # Принудительно задаём модель Qwen
# import os as _os

# _os.environ.setdefault("OLLAMA_MODEL", "qwen2.5:1.5b-instruct")  # для ответов
# _os.environ.setdefault("OLLAMA_EMBED_MODEL", "nomic-embed-text") # для эмбеддингов
# _os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")

# import streamlit as st
# from core.rag_engine import get_answer
# from core.pedagogy import should_hint, generate_hint
# from gui.session_manager import get_session_history
# from llm.quiz_generator import generate_quiz
# from ethics.user_feedback import save_feedback

# from data_ingestion.pdf_loader import extract_text_from_pdf
# from data_ingestion.docx_loader import extract_text_from_docx
# from data_ingestion.splitter import split_text
# from data_ingestion.preprocessor import clean_text


# UPLOAD_DIR = "uploaded_materials"




# import sys, os
# from pathlib import Path
# sys.path.append(str(Path(__file__).parent.parent))
# from config import OLLAMA_MODEL, embedding_model


# import streamlit as st
# from core.rag_engine import get_answer
# from core.pedagogy import should_hint, generate_hint
# from gui.session_manager import get_session_history
# from llm.quiz_generator import generate_quiz
# from ethics.user_feedback import save_feedback

# from data_ingestion.pdf_loader import extract_text_from_pdf
# from data_ingestion.docx_loader import extract_text_from_docx
# from data_ingestion.splitter import split_text
# from data_ingestion.preprocessor import clean_text
# from vector_db.faiss_interface import initialize_index

# UPLOAD_DIR = "uploaded_materials"

# def handle_file_upload():
#     st.subheader("📚 Загрузка учебного материала")
#     uploaded_file = st.file_uploader("Выберите PDF или DOCX файл", type=["pdf", "docx"])
#     if uploaded_file:
#         os.makedirs(UPLOAD_DIR, exist_ok=True)
#         file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
#         with open(file_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
#         st.success(f"Файл '{uploaded_file.name}' загружен успешно!")

#         try:
#             st.write("📄 Извлечение текста из файла...")
#             if uploaded_file.name.endswith(".pdf"):
#                 raw_text = extract_text_from_pdf(file_path)
#             else:
#                 raw_text = extract_text_from_docx(file_path)

#             st.write(f"📜 Извлечено {len(raw_text)} символов текста.")

#             cleaned = clean_text(raw_text)
#             st.write(f"🧹 После очистки: {len(cleaned)} символов.")

#             chunks = split_text(cleaned)
#             st.write(f"🔹 Чанков создано: {len(chunks)}")
#             if chunks:
#                 st.write(f"🧩 Пример чанка:\n\n{chunks[0]}")

#             st.write("🔍 Инициализация индекса...")
#             initialize_index(chunks)

#             st.session_state["documents"] = chunks
#             st.success("Материал проиндексирован и готов к использованию!")
#         except Exception as e:
#             st.error(f"❌ Ошибка при обработке файла: {e}")

# def run_app():
#     st.set_page_config(page_title="StudyBuddy", layout="wide")
#     st.title("📘 StudyBuddy: Интеллектуальный помощник")

#     handle_file_upload()

#     history = get_session_history()
#     tab1, tab2 = st.tabs(["💬 Задать вопрос", "📝 Quiz"])

#     with tab1:
#         st.subheader("Диалог с ассистентом")
#         question = st.text_input("Введите вопрос:")
#         use_pedagogy = st.checkbox("Режим подсказок (не давать решение)", value=True)

#         if st.button("Ответить") and question:
#             if "documents" not in st.session_state or not st.session_state["documents"]:
#                 st.warning("❗ Сначала загрузите и проиндексируйте учебный материал.")
#             else:
#                 if use_pedagogy and should_hint(question):
#                     answer = generate_hint(question)
#                 else:
#                     answer = get_answer(question, st.session_state.chat_history)

#                 history.add_turn(question, answer)
#                 st.markdown(f"**Ответ:** {answer}")
#                 speak(answer)

#                 st.markdown("---")
#                 st.markdown("Оцените ответ:")
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("👍 Полезно"):
#                         save_feedback(question, answer, True)
#                 with col2:
#                     if st.button("👎 Не полезно"):
#                         save_feedback(question, answer, False)

#         st.markdown("### История диалога:")
#         for q, a in history.get_history():
#             st.markdown(f"**Вы:** {q}\n\n**Бот:** {a}")

#     with tab2:
#         st.subheader("Генерация теста по теме")
#         topic = st.text_input("Введите тему для теста:")
#         num_q = st.slider("Количество вопросов", 1, 10, 5)

#         if st.button("Создать Quiz"):
#             quiz = generate_quiz(topic, num_q)
#             st.text_area("Вопросы для самопроверки", quiz, height=300)

# if __name__ == "__main__":
#     run_app()

import os
from pathlib import Path
import sys

# Пути и конфиг
sys.path.append(str(Path(__file__).parent.parent))
from config import embedding_model, OLLAMA_MODEL  # noqa: F401

# Фиксируем модели Ollama (по желанию)
os.environ.setdefault("OLLAMA_MODEL", "qwen2.5:1.5b-instruct")
os.environ.setdefault("OLLAMA_EMBED_MODEL", "nomic-embed-text")
os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")

import streamlit as st
from core.rag_engine import get_answer
from core.pedagogy import should_hint, generate_hint
# from gui.session_manager import get_session_history  # больше не нужен
from llm.quiz_generator import generate_quiz

from data_ingestion.pdf_loader import extract_text_from_pdf
from data_ingestion.docx_loader import extract_text_from_docx
from data_ingestion.splitter import split_text
from data_ingestion.preprocessor import clean_text
from vector_db.faiss_interface import initialize_index

UPLOAD_DIR = "uploaded_materials"

# ===================== In‑memory feedback/mastery ===================== #
def init_feedback_state():
    """Инициализирует структуры для фидбека, мастерства и истории диалога."""
    if "feedback" not in st.session_state:
        st.session_state.feedback = []    # [{q, a, understood, skills}]
    if "mastery" not in st.session_state:
        st.session_state.mastery = {}     # skill -> score
    if "last_answer_bundle" not in st.session_state:
        st.session_state.last_answer_bundle = None  # (q, a, skills)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  # список кортежей (q, a)

def record_feedback(question: str, answer: str, understood: bool, skills=None):
    """Коллбэк для кнопок 'Понятно/Не понятно'."""
    item = {
        "q": question,
        "a": answer,
        "understood": understood,
        "skills": skills or []
    }
    st.session_state.feedback.append(item)
    for s in (item["skills"] or ["general"]):
        st.session_state.mastery[s] = st.session_state.mastery.get(s, 0) + (1 if understood else -1)
# ===================================================================== #

def handle_file_upload():
    st.subheader("📚 Загрузка учебного материала")
    uploaded_file = st.file_uploader("Выберите PDF или DOCX файл", type=["pdf", "docx"])
    if not uploaded_file:
        return

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Файл '{uploaded_file.name}' загружен успешно!")

    try:
        st.write("📄 Извлечение текста из файла...")
        if uploaded_file.name.endswith(".pdf"):
            raw_text = extract_text_from_pdf(file_path)
        else:
            raw_text = extract_text_from_docx(file_path)

        st.write(f"📜 Извлечено {len(raw_text)} символов текста.")
        cleaned = clean_text(raw_text)
        st.write(f"🧹 После очистки: {len(cleaned)} символов.")

        chunks = split_text(cleaned)
        st.write(f"🔹 Чанков создано: {len(chunks)}")
        if chunks:
            st.write(f"🧩 Пример чанка:\n\n{chunks[0]}")

        st.write("🔍 Инициализация индекса...")
        initialize_index(chunks)

        st.session_state["documents"] = chunks
        st.success("Материал проиндексирован и готов к использованию!")
    except Exception as e:
        st.error(f"❌ Ошибка при обработке файла: {e}")

# --- Мягкая подправка текста для TTS (не меняет сам ответ на экране)
def sanitize_for_tts(text: str) -> str:
    low = text.lower()
    if "бит равен 1 байту" in low or "бит = 1 байт" in low:
        text += "\nУточнение: на самом деле 1 байт = 8 бит."
    return text

def run_app():
    st.set_page_config(page_title="StudyBuddy", layout="wide")
    st.title("📘 StudyBuddy: Интеллектуальный помощник")

    # Инициализация in‑memory состояния
    init_feedback_state()

    # Загрузка и индексирование материала
    handle_file_upload()

    tab1, tab2, tab3 = st.tabs(["💬 Задать вопрос", "📝 Quiz", "📈 Прогресс"])

    with tab1:
        st.subheader("Диалог с ассистентом")
        question = st.text_input("Введите вопрос:")
        use_pedagogy = st.checkbox("Режим подсказок (не давать решение)", value=True)

        if st.button("Ответить") and question:
            if "documents" not in st.session_state or not st.session_state["documents"]:
                st.warning("❗ Сначала загрузите и проиндексируйте учебный материал.")
            else:
                if use_pedagogy and should_hint(question):
                    answer = generate_hint(question)
                    skills = None   # можно позже подставлять список тем
                else:
                    answer = get_answer(question, st.session_state.chat_history)
                    skills = None   # TODO: прокинуть темы из retrieve, если есть

                # сохраняем ответ в историю
                st.session_state.chat_history.append((question, answer))
                st.session_state.last_answer_bundle = (question, answer, skills)

                st.markdown(f"**Ответ:** {answer}")
                # Аккуратная озвучка
                try:
                    from output.speech_output import speak
                    safe_answer = sanitize_for_tts(answer)
                    speak(safe_answer, flush=False, debounce_sec=1.0)
                except Exception as e:
                    st.warning(f"❌ Ошибка синтеза речи: {e}")

                st.markdown("---")
                st.markdown("Оцените понятность ответа:")

                col1, col2 = st.columns(2)
                # делаем уникальные ключи для кнопок на каждый ответ
                uid = f"{len(st.session_state.feedback)}_{abs(hash(question)) % 10_000_000}"

                q_cur, a_cur, skills_cur = st.session_state.last_answer_bundle

                col1.button(
                    "👍 Понятно",
                    key=f"fb_ok_{uid}",
                    on_click=record_feedback,
                    args=(q_cur, a_cur, True, skills_cur)
                )
                col2.button(
                    "🤔 Не понятно",
                    key=f"fb_bad_{uid}",
                    on_click=record_feedback,
                    args=(q_cur, a_cur, False, skills_cur)
                )

        # История диалога (чисто из session_state)
        st.markdown("### История диалога:")
        for q, a in st.session_state.chat_history:
            st.markdown(f"**Вы:** {q}\n\n**Бот:** {a}")

    with tab2:
        st.subheader("Генерация теста по теме")
        topic = st.text_input("Введите тему для теста:")
        num_q = st.slider("Количество вопросов", 1, 10, 5)

        if st.button("Создать Quiz"):
            quiz = generate_quiz(topic, num_q)
            st.text_area("Вопросы для самопроверки", quiz, height=300)

    with tab3:
        st.subheader("Ваш прогресс за текущую сессию")

        # Гистограмма по 'мастерству'
        if st.session_state.mastery:
            st.write("**Суммарная динамика по темам** (условные баллы):")
            try:
                import pandas as pd
                df = pd.DataFrame(
                    {"skill": list(st.session_state.mastery.keys()),
                     "score": list(st.session_state.mastery.values())}
                ).set_index("skill")
                st.bar_chart(df)
            except Exception:
                st.json(st.session_state.mastery)
        else:
            st.info("Пока нет данных. Оцените хотя бы один ответ кнопками выше.")

        st.markdown("---")
        st.write("**Оценки ответов:**")
        if st.session_state.feedback:
            try:
                import pandas as pd
                fb_rows = [{
                    "Вопрос": it["q"],
                    "Понятно": "Да" if it["understood"] else "Нет",
                    "Темы": ", ".join(it["skills"]) if it["skills"] else "—"
                } for it in st.session_state.feedback]
                st.dataframe(pd.DataFrame(fb_rows))
            except Exception:
                for it in st.session_state.feedback:
                    st.write(f"- Понятно: {'Да' if it['understood'] else 'Нет'} | Темы: {', '.join(it['skills']) if it['skills'] else '—'}")
                    st.caption(f"Вопрос: {it['q']}")
        else:
            st.write("Ещё нет оценок за эту сессию.")

if __name__ == "__main__":
    run_app()
