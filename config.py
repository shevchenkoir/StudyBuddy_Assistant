# import os
# from dotenv import load_dotenv
# from langchain.embeddings import OllamaEmbeddings
# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_ollama import OllamaEmbeddings
# load_dotenv()

# OLLAMA_MODEL = "llama3.1"
# OLLAMA_BASE_URL = "http://localhost:11434" 
# embedding_model = OllamaEmbeddings(model="llama3.1")

# config.py

import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings  

load_dotenv()

# Конфигурация
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "nomic-embed-text")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = "qwen2.5:1.5b-instruct"


# Инициализация эмбеддингов
embedding_model = OllamaEmbeddings(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=0.1  # опционально
)



