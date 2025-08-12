# # import faiss
# # import numpy as np
# # from vector_db.embedding_model import get_embedding, get_model, documents

# # index = None
# # model = get_model()

# # def initialize_index():
# #     global index
# #     embeddings = [get_embedding(chunk) for chunk in documents]
# #     index = faiss.IndexFlatL2(len(embeddings[0]))
# #     index.add(np.array(embeddings))

# # def search_similar_chunks(query, k=3):
# #     if index is None:
# #         initialize_index()
# #     query_vector = np.array([get_embedding(query)])
# #     D, I = index.search(query_vector, k)
# #     return [documents[i] for i in I[0]]


# import faiss
# import numpy as np
# # from .embedding_model import create_embeddings, get_embedding, documents
# from .embedding_model import get_text_embedding


# index = None
# doc_texts = []

# def initialize_index():
#     global index, doc_texts
#     embeddings = create_embeddings(documents)
#     doc_texts = documents.copy()
#     index = faiss.IndexFlatL2(embeddings[0].shape[0])
#     index.add(np.array(embeddings))

# def search_similar_chunks(query, top_k=5):
#     query_vector = get_embedding(query).reshape(1, -1)
#     D, I = index.search(query_vector, top_k)
#     return [doc_texts[i] for i in I[0]]

# import faiss
# import numpy as np
# from .embedding_model import get_text_embedding

# index = None
# doc_texts = []

# def create_embeddings(texts):
#     embeddings = []
#     for text in texts:
#         emb = get_text_embedding(text)
#         embeddings.append(emb)
#     return np.array(embeddings).astype('float32')

# def initialize_index(documents):
#     global index, doc_texts
#     embeddings = create_embeddings(documents)
#     doc_texts = documents.copy()
#     index = faiss.IndexFlatL2(embeddings.shape[1])
#     index.add(embeddings)

# def search_similar_chunks(query, top_k=5):
#     query_vector = get_text_embedding(query)
#     if not query_vector:
#         return []
#     query_vector = np.array(query_vector).astype('float32').reshape(1, -1)
#     D, I = index.search(query_vector, top_k)
#     return [doc_texts[i] for i in I[0]]





import faiss
import numpy as np
from .embedding_model import get_text_embedding

index = None
doc_texts = []

def create_embeddings(texts):
    embeddings = []
    for i, text in enumerate(texts):
        emb = get_text_embedding(text)
        if not emb:
            print(f"⚠️ Чанк {i} не дал эмбеддинг.")
            continue
        embeddings.append(emb)
    if not embeddings:
        raise ValueError("❌ Не удалось создать ни одного эмбеддинга.")
    return np.array(embeddings).astype('float32')

def initialize_index(documents):
    global index, doc_texts
    print(f"📥 Загружаем {len(documents)} документов для индексации...")
    embeddings = create_embeddings(documents)
    print(f"🔢 Получено {len(embeddings)} эмбеддингов")
    doc_texts = documents.copy()
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    print("✅ Индекс создан.")

def search_similar_chunks(query, top_k=5):
    query_vector = get_text_embedding(query)
    if not query_vector:
        return []
    query_vector = np.array(query_vector).astype('float32').reshape(1, -1)
    D, I = index.search(query_vector, top_k)
    return [doc_texts[i] for i in I[0]]
