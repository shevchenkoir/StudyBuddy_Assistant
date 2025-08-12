

# # # import sys, os
# # # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# # # import streamlit as st
# # # from core.rag_engine import get_answer
# # # from data_ingestion.pdf_loader import extract_text_from_pdf
# # # from data_ingestion.docx_loader import extract_text_from_docx
# # # from data_ingestion.preprocessor import clean_text
# # # from data_ingestion.splitter import split_text
# # # from vector_db.embedding_model import documents
# # # from vector_db.faiss_interface import initialize_index


# # # UPLOAD_DIR = "uploaded_materials"

# # # def run_app():
# # #     st.set_page_config(page_title="StudyBuddy", layout="wide")
# # #     st.title("📘 StudyBuddy: Твой ИИ-тьютор")

# # #     # Инициализация истории
# # #     if "chat_history" not in st.session_state:
# # #         st.session_state.chat_history = []

# # #     # Загрузка и обработка файла
# # #     uploaded_file = st.file_uploader("📚 Загрузите учебный материал (PDF или DOCX)", type=["pdf", "docx"])
# # #     if uploaded_file:
# # #         os.makedirs(UPLOAD_DIR, exist_ok=True)
# # #         file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
# # #         with open(file_path, "wb") as f:
# # #             f.write(uploaded_file.getbuffer())
# # #         st.success(f"Файл '{uploaded_file.name}' успешно загружен!")

# # #         # Извлечение и индексирование текста
# # #         if uploaded_file.name.endswith(".pdf"):
# # #             raw_text = extract_text_from_pdf(file_path)
# # #         else:
# # #             raw_text = extract_text_from_docx(file_path)

# # #         cleaned = clean_text(raw_text)
# # #         chunks = split_text(cleaned)
# # #         documents.clear()
# # #         documents.extend(chunks)
# # #         initialize_index()
# # #         st.success("Материал проиндексирован и готов к использованию!")

# # #     # Ввод вопроса
# # #     st.subheader("💬 Введите вопрос")
# # #     question = st.text_input("Ваш вопрос:")

# # #     if st.button("Отправить") and question:
# # #         st.session_state.chat_history.append({"role": "user", "content": question})
# # #         answer = get_answer(question, st.session_state.chat_history)
# # #         st.session_state.chat_history.append({"role": "assistant", "content": answer})
# # #         st.markdown(f"**Ответ:** {answer}")

# # #     # История
# # #     if st.session_state.chat_history:
# # #         with st.expander("📜 История диалога"):
# # #             for entry in st.session_state.chat_history:
# # #                 role = "🧑" if entry["role"] == "user" else "🤖"
# # #                 st.markdown(f"{role} **{entry['role']}**: {entry['content']}")

# # # # Запуск
# # # if __name__ == "__main__":
# # #     run_app()

# # # from pathlib import Path
# # # import sys, os
# # # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
# # # from vector_db.embedding_model import documents
# # # from vector_db.faiss_interface import initialize_index

# # # from vector_db.embedding_model import documents, create_embeddings
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
# # #             # 📖 Извлечение текста
# # #             if uploaded_file.name.endswith(".pdf"):
# # #                 raw_text = extract_text_from_pdf(file_path)
# # #             else:
# # #                 raw_text = extract_text_from_docx(file_path)

# # #             # 🧹 Очистка и разбиение
# # #             cleaned = clean_text(raw_text)
# # #             chunks = split_text(cleaned)
# # #             documents.clear()
# # #             documents.extend(chunks)

# # #             # 🧠 Генерация эмбеддингов + инициализация поиска
# # #             create_embeddings(documents)
# # #             initialize_index()

# # #             st.success("Материал проиндексирован и готов к использованию!")
# # #         except Exception as e:
# # #             st.error(f"Ошибка при обработке файла: {e}")


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
# # #             if use_pedagogy and should_hint(question):
# # #                 answer = generate_hint(question)
# # #             else:
# # #                 answer = get_answer(question, st.session_state.chat_history)

# # #             history.add_turn(question, answer)
# # #             st.markdown(f"**Ответ:** {answer}")

# # #             st.markdown("---")
# # #             st.markdown("Оцените ответ:")
# # #             col1, col2 = st.columns(2)
# # #             with col1:
# # #                 if st.button("👍 Полезно"):
# # #                     save_feedback(question, answer, True)
# # #             with col2:
# # #                 if st.button("👎 Не полезно"):
# # #                     save_feedback(question, answer, False)

# # #         st.markdown("### История диалога:")
# # #         for q, a in history.get_history():
# # #             st.markdown(f"**Вы:** {q}\\n\\n**Бот:** {a}")

# # #     with tab2:
# # #         st.subheader("Генерация теста по теме")
# # #         topic = st.text_input("Введите тему для теста:")
# # #         num_q = st.slider("Количество вопросов", 1, 10, 5)

# # #         if st.button("Создать Quiz"):
# # #             quiz = generate_quiz(topic, num_q)
# # #             st.text_area("Вопросы для самопроверки", quiz, height=300)

# # # if __name__ == "__main__":
# # #     run_app()

# # # import sys, os
# # # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# # # from config import embedding_model, OLLAMA_MODEL

# # import sys, os
# # from pathlib import Path
# # sys.path.append(str(Path(__file__).parent.parent))
# # from config import embedding_model, OLLAMA_MODEL

# # # Принудительно задаём модель Qwen
# # import os as _os

# # _os.environ.setdefault("OLLAMA_MODEL", "qwen2.5:1.5b-instruct")  # для ответов
# # _os.environ.setdefault("OLLAMA_EMBED_MODEL", "nomic-embed-text") # для эмбеддингов
# # _os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")



# # import streamlit as st
# # from core.rag_engine import get_answer
# # from core.pedagogy import should_hint, generate_hint
# # from gui.session_manager import get_session_history
# # from llm.quiz_generator import generate_quiz
# # from ethics.user_feedback import save_feedback

# # from data_ingestion.pdf_loader import extract_text_from_pdf
# # from data_ingestion.docx_loader import extract_text_from_docx
# # from data_ingestion.splitter import split_text
# # from data_ingestion.preprocessor import clean_text
# # from vector_db.faiss_interface import initialize_index

# # UPLOAD_DIR = "uploaded_materials"




# # import sys, os
# # from pathlib import Path
# # sys.path.append(str(Path(__file__).parent.parent))
# # from config import OLLAMA_MODEL, embedding_model


# # import streamlit as st
# # from core.rag_engine import get_answer
# # from core.pedagogy import should_hint, generate_hint
# # from gui.session_manager import get_session_history
# # from llm.quiz_generator import generate_quiz
# # from ethics.user_feedback import save_feedback

# # from data_ingestion.pdf_loader import extract_text_from_pdf
# # from data_ingestion.docx_loader import extract_text_from_docx
# # from data_ingestion.splitter import split_text
# # from data_ingestion.preprocessor import clean_text
# # from vector_db.faiss_interface import initialize_index

# # UPLOAD_DIR = "uploaded_materials"

# # def handle_file_upload():
# #     st.subheader("📚 Загрузка учебного материала")
# #     uploaded_file = st.file_uploader("Выберите PDF или DOCX файл", type=["pdf", "docx"])
# #     if uploaded_file:
# #         os.makedirs(UPLOAD_DIR, exist_ok=True)
# #         file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
# #         with open(file_path, "wb") as f:
# #             f.write(uploaded_file.getbuffer())
# #         st.success(f"Файл '{uploaded_file.name}' загружен успешно!")

# #         try:
# #             st.write("📄 Извлечение текста из файла...")
# #             if uploaded_file.name.endswith(".pdf"):
# #                 raw_text = extract_text_from_pdf(file_path)
# #             else:
# #                 raw_text = extract_text_from_docx(file_path)

# #             st.write(f"📜 Извлечено {len(raw_text)} символов текста.")

# #             cleaned = clean_text(raw_text)
# #             st.write(f"🧹 После очистки: {len(cleaned)} символов.")

# #             chunks = split_text(cleaned)
# #             st.write(f"🔹 Чанков создано: {len(chunks)}")
# #             if chunks:
# #                 st.write(f"🧩 Пример чанка:\n\n{chunks[0]}")

# #             st.write("🔍 Инициализация индекса...")
# #             initialize_index(chunks)

# #             st.session_state["documents"] = chunks
# #             st.success("Материал проиндексирован и готов к использованию!")
# #         except Exception as e:
# #             st.error(f"❌ Ошибка при обработке файла: {e}")

# # def run_app():
# #     st.set_page_config(page_title="StudyBuddy", layout="wide")
# #     st.title("📘 StudyBuddy: Интеллектуальный помощник")

# #     handle_file_upload()

# #     history = get_session_history()
# #     tab1, tab2 = st.tabs(["💬 Задать вопрос", "📝 Quiz"])

# #     with tab1:
# #         st.subheader("Диалог с ассистентом")
# #         question = st.text_input("Введите вопрос:")
# #         use_pedagogy = st.checkbox("Режим подсказок (не давать решение)", value=True)

# #         if st.button("Ответить") and question:
# #             if "documents" not in st.session_state or not st.session_state["documents"]:
# #                 st.warning("❗ Сначала загрузите и проиндексируйте учебный материал.")
# #             else:
# #                 if use_pedagogy and should_hint(question):
# #                     answer = generate_hint(question)
# #                 else:
# #                     answer = get_answer(question, st.session_state.chat_history)

# #                 history.add_turn(question, answer)
# #                 st.markdown(f"**Ответ:** {answer}")

# #                 st.markdown("---")
# #                 st.markdown("Оцените ответ:")
# #                 col1, col2 = st.columns(2)
# #                 with col1:
# #                     if st.button("👍 Полезно"):
# #                         save_feedback(question, answer, True)
# #                 with col2:
# #                     if st.button("👎 Не полезно"):
# #                         save_feedback(question, answer, False)

# #         st.markdown("### История диалога:")
# #         for q, a in history.get_history():
# #             st.markdown(f"**Вы:** {q}\n\n**Бот:** {a}")

# #     with tab2:
# #         st.subheader("Генерация теста по теме")
# #         topic = st.text_input("Введите тему для теста:")
# #         num_q = st.slider("Количество вопросов", 1, 10, 5)

# #         if st.button("Создать Quiz"):
# #             quiz = generate_quiz(topic, num_q)
# #             st.text_area("Вопросы для самопроверки", quiz, height=300)

# # if __name__ == "__main__":
# #     run_app()
import sys, os
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import embedding_model, OLLAMA_MODEL
from output.speech_output import speak

# Принудительно задаём модель Qwen
import os as _os

_os.environ.setdefault("OLLAMA_MODEL", "qwen2.5:1.5b-instruct")  # для ответов
_os.environ.setdefault("OLLAMA_EMBED_MODEL", "nomic-embed-text") # для эмбеддингов
_os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")

import streamlit as st
from core.rag_engine import get_answer
from core.pedagogy import should_hint, generate_hint
from gui.session_manager import get_session_history
from llm.quiz_generator import generate_quiz
from ethics.user_feedback import save_feedback

from data_ingestion.pdf_loader import extract_text_from_pdf
from data_ingestion.docx_loader import extract_text_from_docx
from data_ingestion.splitter import split_text
from data_ingestion.preprocessor import clean_text


UPLOAD_DIR = "uploaded_materials"




import sys, os
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import OLLAMA_MODEL, embedding_model


import streamlit as st
from core.rag_engine import get_answer
from core.pedagogy import should_hint, generate_hint
from gui.session_manager import get_session_history
from llm.quiz_generator import generate_quiz
from ethics.user_feedback import save_feedback

from data_ingestion.pdf_loader import extract_text_from_pdf
from data_ingestion.docx_loader import extract_text_from_docx
from data_ingestion.splitter import split_text
from data_ingestion.preprocessor import clean_text
from vector_db.faiss_interface import initialize_index

UPLOAD_DIR = "uploaded_materials"

def handle_file_upload():
    st.subheader("📚 Загрузка учебного материала")
    uploaded_file = st.file_uploader("Выберите PDF или DOCX файл", type=["pdf", "docx"])
    if uploaded_file:
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

def run_app():
    st.set_page_config(page_title="StudyBuddy", layout="wide")
    st.title("📘 StudyBuddy: Интеллектуальный помощник")

    handle_file_upload()

    history = get_session_history()
    tab1, tab2 = st.tabs(["💬 Задать вопрос", "📝 Quiz"])

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
                else:
                    answer = get_answer(question, st.session_state.chat_history)

                history.add_turn(question, answer)
                st.markdown(f"**Ответ:** {answer}")
                speak(answer)

                st.markdown("---")
                st.markdown("Оцените ответ:")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👍 Полезно"):
                        save_feedback(question, answer, True)
                with col2:
                    if st.button("👎 Не полезно"):
                        save_feedback(question, answer, False)

        st.markdown("### История диалога:")
        for q, a in history.get_history():
            st.markdown(f"**Вы:** {q}\n\n**Бот:** {a}")

    with tab2:
        st.subheader("Генерация теста по теме")
        topic = st.text_input("Введите тему для теста:")
        num_q = st.slider("Количество вопросов", 1, 10, 5)

        if st.button("Создать Quiz"):
            quiz = generate_quiz(topic, num_q)
            st.text_area("Вопросы для самопроверки", quiz, height=300)

if __name__ == "__main__":
    run_app()

