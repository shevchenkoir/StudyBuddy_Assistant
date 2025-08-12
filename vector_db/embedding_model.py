
# # # # import os
# # # # from dotenv import load_dotenv
# # # # # from langchain_community.embeddings import OllamaEmbeddings
# # # # from langchain_ollama import OllamaEmbeddings
# # # # from typing import List

# # # # load_dotenv()

# # # # # Явно указываем версию модели
# # # # OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:latest")
# # # # # OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "nomic-embed-text")
# # # # OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# # # # # Инициализация с обработкой ошибок
# # # # try:
# # # #     embedding_model = OllamaEmbeddings(
# # # #         model=OLLAMA_MODEL,
# # # #         base_url=OLLAMA_BASE_URL,
# # # #         temperature=0.1
# # # #     )
    
# # # # except Exception as e:
# # # #     print(f"❌ Ошибка инициализации Ollama: {e}")
# # # #     embedding_model = None

# # # # def get_text_embedding(text: str) -> List[float]:
# # # #     """Генерация эмбеддинга с проверкой модели"""
# # # #     if not embedding_model:
# # # #         print("⚠️ Модель не инициализирована")
# # # #         return []
    
# # # #     try:
# # # #         return embedding_model.embed_query(text)
# # # #     except Exception as e:
# # # #         print(f"❌ Ошибка генерации: {e}")
# # # #         print(f"Проверьте модель: ollama run {OLLAMA_MODEL}")
# # # #         return []




# # # import os
# # # from dotenv import load_dotenv
# # # from langchain_ollama import OllamaEmbeddings
# # # from typing import List

# # # load_dotenv()

# # # OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "nomic-embed-text")
# # # OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# # # try:
# # #     embedding_model = OllamaEmbeddings(
# # #         model=OLLAMA_MODEL,
# # #         base_url=OLLAMA_BASE_URL,
# # #         temperature=0.1
# # #     )
# # #     print(f"✅ Модель эмбеддингов: {OLLAMA_MODEL}")
# # # except Exception as e:
# # #     print(f"❌ Ошибка инициализации Ollama: {e}")
# # #     embedding_model = None

# # # def get_text_embedding(text: str) -> List[float]:
# # #     if not embedding_model:
# # #         print("⚠️ Модель не инициализирована")
# # #         return []
    
# # #     try:
# # #         print(f"📌 Входной текст: {text[:30]}...")
# # #         vector = embedding_model.embed_query(text)
# # #         print(f"📌 Эмбеддинг (длина): {len(vector)}")
# # #         return vector
# # #     except Exception as e:
# # #         print(f"❌ Ошибка генерации эмбеддинга: {e}")
# # #         print(f"Проверьте модель: ollama run {OLLAMA_MODEL}")
# # #         return []

# # # from sentence_transformers import SentenceTransformer
# # # from typing import List

# # # model = SentenceTransformer('all-MiniLM-L6-v2')

# # # def get_text_embedding(text: str) -> List[float]:
# # #     try:
# # #         print(f"📌 Входной текст: {text[:30]}...")
# # #         vector = model.encode(text).tolist()
# # #         print(f"📌 Эмбеддинг (длина): {len(vector)}")
# # #         return vector
# # #     except Exception as e:
# # #         print(f"❌ Ошибка генерации эмбеддинга: {e}")
# # #         return []



# # import os
# # from dotenv import load_dotenv
# # from typing import List
# # from langchain_ollama import OllamaEmbeddings

# # load_dotenv()

# # # Модель для эмбеддингов
# # OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
# # OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# # try:
# #     embedding_model = OllamaEmbeddings(
# #         model=OLLAMA_EMBED_MODEL,
# #         base_url=OLLAMA_BASE_URL
# #     )
# #     print(f"✅ Модель эмбеддингов: {OLLAMA_EMBED_MODEL}")
# # except Exception as e:
# #     print(f"❌ Ошибка инициализации Ollama Embeddings: {e}")
# #     embedding_model = None

# # def get_text_embedding(text: str) -> List[float]:
# #     """Генерация эмбеддинга с проверкой модели"""
# #     if not embedding_model:
# #         print("⚠️ Модель эмбеддингов не инициализирована")
# #         return []
# #     try:
# #         return embedding_model.embed_query(text)
# #     except Exception as e:
# #         print(f"❌ Ошибка генерации эмбеддинга: {e}")
# #         print(f"Проверьте модель: ollama run {OLLAMA_EMBED_MODEL}")
# #         return []



# # vector_db/embedding_model.py
# import os
# from typing import List
# from functools import lru_cache

# from dotenv import load_dotenv
# load_dotenv()

# # Можно подменить модель через .env, дефолт — лёгкая и стабильная
# EMBEDDING_MODEL_ID = os.getenv("EMBEDDING_MODEL_ID", "sentence-transformers/all-MiniLM-L6-v2")

# @lru_cache(maxsize=1)
# def _load_model():
#     """
#     Ленивая загрузка модели эмбеддингов один раз на процесс.
#     Не требует Ollama. Работает офлайн.
#     """
#     from sentence_transformers import SentenceTransformer
#     # загружаем по короткому id тоже (и полный, и короткий работают)
#     model_name = EMBEDDING_MODEL_ID.split("/")[-1]
#     try:
#         model = SentenceTransformer(EMBEDDING_MODEL_ID)
#     except Exception:
#         # fallback на короткое имя, если полный путь не сработал
#         model = SentenceTransformer(model_name)
#     return model

# def get_text_embedding(text: str) -> List[float]:
#     """
#     Возвращает эмбеддинг текста как список float.
#     При ошибке — пустой список (чтобы индексатор мог пропустить неудачные чанки).
#     """
#     text = (text or "").strip()
#     if not text:
#         return []
#     try:
#         model = _load_model()
#         vec = model.encode(text, normalize_embeddings=True)  # нормализация — полезна для L2
#         return vec.astype("float32").tolist()
#     except Exception as e:
#         print(f"❌ Ошибка генерации эмбеддинга (sentence-transformers): {e}")



import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from typing import List

load_dotenv()

# Модель для эмбеддингов — лёгкая
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL_EMBED", "nomic-embed-text")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

try:
    embedding_model = OllamaEmbeddings(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL
    )
except Exception as e:
    print(f"❌ Ошибка инициализации Ollama: {e}")
    embedding_model = None

def get_text_embedding(text: str) -> List[float]:
    if not embedding_model:
        print("⚠️ Модель эмбеддингов не инициализирована")
        return []
    try:
        return embedding_model.embed_query(text)
    except Exception as e:
        print(f"❌ Ошибка генерации эмбеддинга: {e}")
        print(f"Проверьте модель: ollama run {OLLAMA_MODEL}")
        return []
