# 📘 StudyBuddy Assistant

**StudyBuddy** — интеллектуальный ассистент-тьютор на базе **LLM** и **RAG**, помогающий студентам осваивать учебный материал.

## 💡 Возможности
- 📖 **Отвечает** на вопросы по загруженному материалу.
- 🎓 Даёт **педагогические подсказки** вместо готовых решений.
- 📝 Генерирует **тренировочные квизы** по темам.
- 🖥 Работает **локально и офлайн** с использованием **Ollama** и **FAISS**.
- 🗣 Поддержка голосового вывода.

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
1. **Активируйте виртуальное окружение**
2. 
   ```powershell
   .venv\Scripts\activate
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
│   ├── 📄 main.py                       # 🚀 Основная точка входа (запуск Streamlit/бота)
│   └── 📄 telegram_bot.py               # 🤖 Telegram-бот
│
├── 📁 assets/                           # 🖼 Статические ресурсы
│
├── 📁 core/                             # 🧠 Основная логика
│   ├── 📄 chat_context.py               # 💬 Контекст диалога
│   ├── 📄 pedagogy.py                   # 📚 Педагогические подсказки
│   ├── 📄 prompt_manager.py             # 📝 Управление промптами
│   ├── 📄 rag_engine.py                 # 🔍 RAG-поиск с OCR, роутингом по курсам и фолбэком
│   └── 📄 router.py                     # 🗺 Маршрутизация вопроса к курсу (math/physics/general)
│
├── 📁 data_ingestion/                   # 📥 Загрузка и индексация данных
│   ├── 📄 build_index.py                 # 🏗 Индексация материалов по курсам
│   ├── 📄 docx_loader.py                # 📄 DOCX-загрузчик
│   ├── 📄 pdf_loader.py                 # 📑 PDF-загрузчик
│   ├── 📄 preprocessor.py               # 🧹 Очистка текста
│   └── 📄 splitter.py                    # ✂ Разделение текста на чанки
│
├── 📁 ethics/                           # ⚖ Этика и обратная связь
│   ├── 📄 solution_filter.py            # 🚫 Фильтрация "списывания"
│   └── 📄 user_feedback.py              # 🗣 Обратная связь от пользователя
│
├── 📁 gui/                              # 🖼 Интерфейс пользователя
│   ├── 📄 helpers_new_formats.py        # 🛠 Хелперы для GUI
│   ├── 📄 session_manager.py            # 📂 Менеджер сессий
│   └── 📄 streamlit_app.py              # 🌐 Streamlit-приложение с вкладками: текст/изображение/quiz
│
├── 📁 llm/                              # 🤖 Взаимодействие с LLM
│   ├── 📄 answer_generator.py           # ✏ Генерация ответа по контексту
│   ├── 📄 ollama_client.py              # 🔌 Клиент для Ollama API (chat/embeddings)
│   └── 📄 quiz_generator.py             # 📝 Генератор тестов по темам
│
├── 📁 Ollama/                           # 📦 Модели и данные Ollama (локальное хранение)
│
├── 📁 output/                           # 🔊 Вывод
│   └── 📄 speech_output.py              # 🗣 Синтез речи (TTS) с защитой от повторного запуска
│
├── 📁 uploaded_materials/               # 📤 Загруженные учебные материалы по курсам
│   ├── 📁 math/
│   ├── 📁 physics/
│   └── 📁 general/
│
├── 📁 utils/                            # 🛠 Утилиты
│   ├── 📄 constants.py                  # 📌 Константы
│   ├── 📄 helpers.py                    # 🔧 Вспомогательные функции
│   ├── 📄 image_ocr.py                   # 🔍 OCR-распознавание изображений (Pillow + OpenCV + Tesseract)
│   └── 📄 interface.py                  # 🔄 Интерфейс для интеграции модулей
│
├── 📁 vector_db/                        # 📊 Векторная база данных (FAISS)
│   ├── 📄 embedding_model.py            # 🧩 Модель эмбеддингов (через Ollama embeddings API)
│   └── 📄 faiss_interface.py            # 📈 Индексация/поиск по курсам и фолбэк по всем индексам
│
├── 📄 .env                              # ⚙ Переменные окружения (модели, путь к Tesseract и т.д.)
├── 📄 check_ollama_connection.py        # 🧪 Проверка доступности Ollama и моделей
├── 📄 config.py                         # ⚙ Общая конфигурация проекта
├── 📄 README.md                         # 📖 Документация
└── 📄 requirements.txt                  # 📦 Список зависимостей

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
