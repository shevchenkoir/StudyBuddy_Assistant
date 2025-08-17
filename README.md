# 📘 StudyBuddy Assistant

**StudyBuddy** — интеллектуальный ассистент-тьютор на базе **LLM** и **RAG**, помогающий студентам осваивать учебный материал.

## 💡 Возможности
- 📖 **Отвечает** на вопросы по загруженному материалу.
- 🎓 Даёт **педагогические подсказки** вместо готовых решений.
- 📝 Генерирует **тренировочные квизы** по темам.
- 🖥 Работает **локально и офлайн** с использованием **Ollama** и **FAISS**.

---

## 🛠 Технологии
- **Python 3.12**
- **Streamlit** — веб-интерфейс.
- **Ollama** — локальный LLM сервер.
- **FAISS** — векторная база данных.
- **pyttsx3** — синтез речи.
- **dotenv** — управление переменными окружения.

---

## 🚀 Запуск проекта

### 1️⃣ Подготовка окружения
1. **Клонирование репозитория и установка зависимостей**
 ```bash
  git clone https://github.com/Study-Buddy.git
  cd Study-Buddy
  python -m venv .venv
  .\.venv\Scripts\activate
```
   
3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

---

### 2️⃣ Запуск в автоматическом режиме (рекомендуется)
Выполните:
```bash
python app/main.py
```
Что произойдёт:
- Запустится `check_ollama_connection.py`:
  - Проверит доступность Ollama.
  - При необходимости запустит `ollama serve`.
  - Проверит наличие моделей:
    - `qwen2.5:1.5b-instruct`
    - `nomic-embed-text`
  - Скачает их, если не установлены.
- После проверки и прогрева моделей запустит веб-интерфейс (`gui/streamlit_app.py`) на `http://localhost:8501`.

---

### 3️⃣ Запуск по-старому (без `main.py`)
Если хотите запускать только веб-интерфейс без автоматической проверки моделей:
```bash
streamlit run gui/streamlit_app.py
```

---

## 📂 Структура проекта
```text
StudyBuddy_Assistant/
├── 📁 app/                              # 🖥 Логика запуска
│   ├── 📄 main.py                       # 🚀 Основная точка входа
│   └── 📄 telegram_bot.py               # 🤖 Telegram-бот
├── 📁 assets/                           # 🖼 Статические ресурсы
├── 📁 core/                             # 🧠 Основная логика
│   ├── 📄 chat_context.py               # 💬 Контекст диалога
│   ├── 📄 pedagogy.py                   # 📚 Педагогические подсказки
│   ├── 📄 prompt_manager.py             # 📝 Управление промптами
│   └── 📄 rag_engine.py                 # 🔍 RAG-поиск
├── 📁 data_ingestion/                   # 📥 Загрузка данных
│   ├── 📄 docx_loader.py                # 📄 DOCX-загрузчик
│   ├── 📄 pdf_loader.py                 # 📑 PDF-загрузчик
│   ├── 📄 preprocessor.py               # 🧹 Очистка текста
│   └── 📄 splitter.py                   # ✂ Разделение на чанки
├── 📁 ethics/                           # ⚖ Этика
│   ├── 📄 solution_filter.py            # 🚫 Фильтрация
│   └── 📄 user_feedback.py              # 🗣 Обратная связь
├── 📁 gui/                              # 🖼 Интерфейс
│   ├── 📄 helpers_new_formats.py        # 🛠 Хелперы GUI
│   ├── 📄 session_manager.py            # 📂 Менеджер сессий
│   └── 📄 streamlit_app.py              # 🌐 Streamlit-приложение
├── 📁 llm/                              # 🤖 Работа с LLM
│   ├── 📄 answer_generator.py           # ✏ Генерация ответов
│   ├── 📄 ollama_client.py              # 🔌 API Ollama
│   └── 📄 quiz_generator.py             # 📝 Генератор тестов
├── 📁 Ollama/                           # 📦 Данные и модели Ollama
├── 📁 output/                           # 🔊 Вывод
│   └── 📄 speech_output.py              # 🗣 Синтез речи
├── 📁 uploaded_materials/               # 📤 Загруженные материалы
├── 📁 utils/                            # 🛠 Утилиты
│   ├── 📄 constants.py                  # 📌 Константы
│   ├── 📄 helpers.py                    # 🔧 Хелперы
│   ├── 📄 image_ocr.py                   # 🔍 OCR-распознавание
│   └── 📄 interface.py                  # 🔄 Интерфейс
├── 📁 vector_db/                        # 📊 Векторная база
│   ├── 📄 embedding_model.py            # 🧩 Модель эмбеддингов
│   └── 📄 faiss_interface.py            # 📈 Работа с FAISS
├── 📄 .env                              # ⚙ Переменные окружения
├── 📄 check_ollama_connection.py        # 🧪 Автопроверка Ollama и моделей
├── 📄 config.py                         # ⚙ Конфигурация
├── 📄 README.md                         # 📖 Документация
└── 📄 requirements.txt                  # 📦 Зависимости
```

---

## 📄 Файл `.env`
```ini
# Модель генерации ответов
OLLAMA_MODEL=qwen2.5:1.5b-instruct
# Модель эмбеддингов
OLLAMA_EMBED_MODEL=nomic-embed-text
# URL Ollama API
OLLAMA_BASE_URL=http://localhost:11434
# Скорость TTS (слов в минуту)
TTS_RATE=175
```
