# # # import requests
# # # import time
# # # from pprint import pprint

# # # OLLAMA_URL = "http://localhost:11434"
# # # MODEL_NAME = "llama3.1:latest"  # Явно указываем версию
# # # TIMEOUT = 15  # Увеличиваем таймаут для медленных систем

# # # def check_server():
# # #     """Проверяет доступность сервера Ollama"""
# # #     try:
# # #         start_time = time.time()
# # #         response = requests.get(f"{OLLAMA_URL}/", timeout=TIMEOUT)
# # #         elapsed = (time.time() - start_time) * 1000
        
# # #         if response.status_code == 200:
# # #             print(f"✅ Сервер Ollama доступен (порт 11434). Время ответа: {elapsed:.0f}мс")
# # #             print(f"Версия сервера: {response.text.strip()}")
# # #             return True
        
# # #         print(f"❌ Неожиданный ответ: HTTP {response.status_code}")
# # #         return False

# # #     except requests.exceptions.RequestException as e:
# # #         print(f"❌ Ошибка подключения к Ollama: {type(e).__name__}")
# # #         print("→ Проверьте что:")
# # #         print("1. Сервер запущен: ollama serve")
# # #         print("2. Порт 11434 не занят другим процессом")
# # #         return False

# # # def check_model():
# # #     """Проверяет работоспособность модели"""
# # #     try:
# # #         print(f"\n🔍 Проверяем модель '{MODEL_NAME}'...")
        
# # #         # 1. Проверяем наличие модели
# # #         models = requests.get(f"{OLLAMA_URL}/api/tags", timeout=TIMEOUT).json()
# # #         if not any(m['name'] == MODEL_NAME for m in models.get('models', [])):
# # #             print(f"❌ Модель '{MODEL_NAME}' не найдена на сервере")
# # #             print("Доступные модели:")
# # #             pprint(models)
# # #             return False

# # #         # 2. Проверяем генерацию
# # #         start_time = time.time()
# # #         response = requests.post(
# # #             f"{OLLAMA_URL}/api/generate",
# # #             json={
# # #                 "model": MODEL_NAME,
# # #                 "prompt": "Напиши одно предложение о Python",
# # #                 "stream": False
# # #             },
# # #             timeout=TIMEOUT
# # #         )
# # #         elapsed = (time.time() - start_time) * 1000

# # #         if response.status_code == 200:
# # #             result = response.json()
# # #             print(f"✅ Модель работает. Время ответа: {elapsed:.0f}мс")
# # #             print(f"Ответ модели: {result['response']}")
# # #             return True
            
# # #         print(f"⚠️ Ошибка генерации: HTTP {response.status_code}")
# # #         pprint(response.json())
# # #         return False

# # #     except requests.exceptions.RequestException as e:
# # #         print(f"❌ Ошибка при проверке модели: {type(e).__name__}")
# # #         print(f"→ Убедитесь что модель загружена: ollama run {MODEL_NAME}")
# # #         return False

# # # if __name__ == "__main__":
# # #     print(f"🔄 Проверка подключения к Ollama ({OLLAMA_URL})...")
# # #     if check_server():
# # #         check_model()


# # import requests
# # import time
# # from pprint import pprint

# # OLLAMA_URL = "http://localhost:11434"
# # MODEL_NAME = "llama3.1:latest"
# # TIMEOUT = 60  # Увеличено для медленных систем

# # def check_connection():
# #     print(f"\n🔍 Проверка подключения к Ollama ({OLLAMA_URL})")
    
# #     try:
# #         # Проверка сервера
# #         start = time.time()
# #         resp = requests.get(f"{OLLAMA_URL}/", timeout=10)
# #         print(f"✅ Сервер: HTTP {resp.status_code} ({time.time()-start:.1f}s)")
# #         print(f"Версия: {resp.text.strip()}")

# #         # Проверка списка моделей
# #         models = requests.get(f"{OLLAMA_URL}/api/tags", timeout=10).json()
# #         print(f"\n📚 Доступные модели:")
# #         for model in models.get('models', []):
# #             print(f"- {model['name']} ({model['size']/1e9:.1f}GB)")

# #         # Проверка генерации
# #         print(f"\n🔥 Тестируем генерацию текста...")
# #         start = time.time()
# #         response = requests.post(
# #             f"{OLLAMA_URL}/api/generate",
# #             json={
# #                 "model": MODEL_NAME,
# #                 "prompt": "Ответь одним словом: Как дела?",
# #                 "stream": False
# #             },
# #             timeout=TIMEOUT
# #         )
        
# #         if response.status_code == 200:
# #             print(f"✅ Успех! Ответ за {time.time()-start:.1f}s:")
# #             print(response.json().get('response', 'Пустой ответ'))
# #         else:
# #             print(f"❌ Ошибка HTTP {response.status_code}:")
# #             pprint(response.json())

# #     except requests.exceptions.Timeout:
# #         print(f"\n⏳ Таймаут ожидания ({TIMEOUT}s)! Попробуйте:")
# #         print("1. Увеличьте TIMEOUT в скрипте")
# #         print("2. Проверьте что 'ollama run llama3.1' запущен в отдельном терминале")
# #     except Exception as e:
# #         print(f"\n💥 Критическая ошибка: {type(e).__name__}")
# #         print("Советы:")
# #         print("- Запустите 'ollama serve' в отдельном окне")
# #         print("- Проверьте 'ollama ps' на наличие работающих процессов")

# # if __name__ == "__main__":
# #     check_connection()



# import requests, json, time

# BASE = "http://localhost:11434"

# def ok(msg): print(f"✅ {msg}")
# def err(msg): print(f"❌ {msg}")
# def info(msg): print(f"🔍 {msg}")

# def post(path, payload):
#     resp = requests.post(BASE + path, json=payload, timeout=60)
#     # Для /api/generate и /api/chat Ollama стримит строки JSON по строкам
#     # Попробуем построчно разобрать поток:
#     text = []
#     for line in resp.iter_lines(decode_unicode=True):
#         if not line: continue
#         try:
#             obj = json.loads(line)
#             text.append(obj.get("message", {}).get("content") or obj.get("response") or "")
#         except json.JSONDecodeError:
#             text.append(line)
#     return resp.status_code, "".join(text).strip()

# def main():
#     info(f"Проверка подключения к Ollama ({BASE})")
#     r = requests.get(BASE, timeout=10)
#     if r.status_code == 200:
#         ok(f"Сервер: HTTP 200 ({r.text.strip()})")
#     else:
#         return err(f"Сервер недоступен: HTTP {r.status_code}")

#     # list models
#     r = requests.get(BASE + "/api/tags", timeout=10)
#     if r.status_code != 200:
#         return err(f"/api/tags: HTTP {r.status_code}")
#     data = r.json()
#     models = [m["name"] for m in data.get("models", [])]
#     print("\n📚 Доступные модели:")
#     for m in models:
#         print("-", m)
#     if not models:
#         return err("Нет моделей. Выполни: ollama pull qwen2.5:0.5b-instruct")

#     # test generate
#     print("\n🔥 Тестируем генерацию текста (POST /api/chat)...")
#     code, out = post("/api/chat", {
#         "model": "qwen2.5:0.5b-instruct",
#         "messages": [{"role":"user","content":"Скажи коротко 'Привет'"}]
#     })
#     if code == 200 and out:
#         ok(f"Генерация ОК: {out[:120]}")
#     else:
#         err(f"Ошибка генерации: HTTP {code} / Ответ: {out[:200]}")

#     # test embeddings
#     print("\n🧠 Тестируем эмбеддинги (POST /api/embeddings)...")
#     r = requests.post(BASE + "/api/embeddings", json={
#         "model": "nomic-embed-text",
#         "prompt": "hello world"
#     }, timeout=30)
#     if r.status_code == 200 and "embedding" in r.json():
#         ok("Эмбеддинги ОК")
#     else:
#         err(f"Эмбеддинги: HTTP {r.status_code} / {r.text[:200]}")

# if __name__ == "__main__":
#     main()



# ollama_check_and_autostart.py
# check_ollama_connection.py
# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import platform
import subprocess
import shutil
import requests
from typing import List, Set

# ===== Настройки =====
BASE = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
GEN_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b-instruct")
EMB_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text:latest")
AUTO_OPEN_INTERACTIVE_RUN = True  # Открыть отдельное окно с `ollama run qwen2.5:1.5b-instruct`

TIMEOUT_SHORT = 10
TIMEOUT_LONG = 60

def ok(msg): print(f"✅ {msg}")
def err(msg): print(f"❌ {msg}")
def info(msg): print(f"🔍 {msg}")

def _cmd_exists(cmd: str) -> bool:
    return shutil.which(cmd) is not None

# ---------- Сервер ----------
def start_ollama_server_if_needed() -> bool:
    """Поднять ollama serve, если сервер не отвечает."""
    try:
        r = requests.get(BASE, timeout=TIMEOUT_SHORT)
        if r.status_code == 200:
            ok(f"Ollama уже работает ({r.text.strip()})")
            return True
    except requests.RequestException:
        pass

    if not _cmd_exists("ollama"):
        err("Команда 'ollama' не найдена в PATH. Установите Ollama и перезапустите.")
        return False

    info("Сервер не отвечает. Запускаю `ollama serve`...")
    try:
        creationflags = 0
        startupinfo = None
        if platform.system() == "Windows":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            creationflags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP

        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            startupinfo=startupinfo,
            creationflags=creationflags
        )

        # Ждём готовности
        for _ in range(30):
            try:
                r = requests.get(BASE, timeout=2)
                if r.status_code == 200:
                    ok("Сервер Ollama запущен.")
                    return True
            except requests.RequestException:
                pass
            time.sleep(1)
        err("Не удалось дождаться запуска Ollama (проверьте `ollama serve`).")
        return False
    except Exception as e:
        err(f"Ошибка запуска Ollama: {e}")
        return False

# ---------- Модели ----------
def _fetch_models() -> List[dict]:
    r = requests.get(f"{BASE}/api/tags", timeout=TIMEOUT_SHORT)
    r.raise_for_status()
    return r.json().get("models", [])

def _norm_variants(name: str) -> Set[str]:
    """Варианты имени: base, base:latest, исходная строка."""
    base = name.split(":", 1)[0]
    return {base, f"{base}:latest", name}

def get_installed_models_set() -> Set[str]:
    """Множество нормализованных имён всех установленных моделей."""
    try:
        models = _fetch_models()
    except Exception as e:
        err(f"Не удалось получить список моделей: {e}")
        return set()

    s: Set[str] = set()
    for m in models:
        raw = m.get("model") or m.get("name")
        if raw:
            if ":" not in raw and "tag" in m:
                raw = f"{raw}:{m['tag']}"
            s |= _norm_variants(raw)
    return s

def ensure_model(model: str) -> bool:
    """Проверяет наличие модели (с учётом :latest), при отсутствии — `ollama pull`."""
    installed = get_installed_models_set()
    if model in installed or any(v in installed for v in _norm_variants(model)):
        ok(f"Модель уже установлена: {model}")
        return True

    info(f"Модель '{model}' не найдена. Загружаю: `ollama pull {model}`")
    try:
        with subprocess.Popen(["ollama", "pull", model],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              text=True) as p:
            for line in p.stdout:
                print(line.rstrip())
    except FileNotFoundError:
        err("Команда 'ollama' не найдена. Добавьте Ollama в PATH.")
        return False
    except Exception as e:
        err(f"Ошибка при загрузке модели '{model}': {e}")
        return False

    # Иногда метаданные прописываются не сразу — делаем несколько повторных проверок
    for _ in range(8):
        time.sleep(1.0)
        installed = get_installed_models_set()
        if model in installed or any(v in installed for v in _norm_variants(model)):
            ok(f"Модель успешно загружена: {model}")
            return True

    err(f"Модель '{model}' не появилась после pull.")
    return False

# ---------- Прогрев ----------
def warmup_chat(model: str) -> bool:
    """Нестримиовый вызов /api/chat — надёжно для парсинга."""
    try:
        r = requests.post(
            f"{BASE}/api/chat",
            json={
                "model": model,
                "messages": [{"role": "user", "content": "Скажи одно слово: Привет"}],
                "stream": False
            },
            timeout=TIMEOUT_LONG
        )
        if r.status_code == 200:
            ok(f"Генерация текста работает ({model}).")
            return True
        err(f"Ошибка chat API: HTTP {r.status_code} — {r.text[:200]}")
        return False
    except Exception as e:
        err(f"Сбой chat API: {e}")
        return False

def warmup_embeddings(model: str) -> bool:
    try:
        r = requests.post(
            f"{BASE}/api/embeddings",
            json={"model": model, "prompt": "hello world"},
            timeout=TIMEOUT_SHORT
        )
        if r.status_code == 200 and "embedding" in r.json():
            ok(f"Эмбеддинги работают ({model}).")
            return True
        err(f"Ошибка embeddings API: HTTP {r.status_code} — {r.text[:200]}")
        return False
    except Exception as e:
        err(f"Сбой embeddings API: {e}")
        return False

# ---------- Интерактивный run ----------
def open_interactive_run(model: str):
    """Открыть отдельное окно с интерактивной сессией `ollama run <model>`."""
    if not _cmd_exists("ollama"):
        err("Не удалось открыть интерактивный run: 'ollama' не найден")
        return
    info(f"Открываю окно с `ollama run {model}`...")
    try:
        system = platform.system()
        if system == "Windows":
            subprocess.Popen(["cmd", "/c", "start", "cmd", "/k", f"ollama run {model}"])
        elif system == "Darwin":
            osa = f'tell application "Terminal" to do script "ollama run {model}"'
            subprocess.Popen(["osascript", "-e", osa])
        else:
            term = shutil.which("gnome-terminal") or shutil.which("xterm")
            if term and os.getenv("DISPLAY"):
                if "gnome-terminal" in term:
                    subprocess.Popen([term, "--", "bash", "-lc", f"ollama run {model}"])
                else:
                    subprocess.Popen([term, "-e", f"bash -lc 'ollama run {model}'"])
            else:
                # без GUI-терминала — просто стартуем фоном
                subprocess.Popen(["ollama", "run", model])
        ok("Интерактивное окно запущено.")
    except Exception as e:
        err(f"Не удалось открыть интерактивный run: {e}")

# ---------- Главный сценарий ----------
def print_models_table():
    models = sorted(get_installed_models_set())
    print("📚 Доступные модели:")
    if not models:
        print("—")
    else:
        for m in models:
            print(f"- {m}")

def main():
    info(f"Проверка подключения к Ollama ({BASE})")
    if not start_ollama_server_if_needed():
        sys.exit(1)

    print_models_table()

    # Гарантируем наличие обеих моделей
    ok_models = True
    ok_models &= ensure_model(GEN_MODEL)
    ok_models &= ensure_model(EMB_MODEL)
    if not ok_models:
        err("Не все требуемые модели удалось подготовить.")
        sys.exit(2)

    # Прогрев API
    warmup_chat(GEN_MODEL)
    warmup_embeddings(EMB_MODEL)

    # Открыть интерактивный run генеративной модели (как вы просили)
    if AUTO_OPEN_INTERACTIVE_RUN:
        open_interactive_run(GEN_MODEL)

    ok("Готово: Ollama доступен, модели есть, прогрев выполнен.")

if __name__ == "__main__":
    main()

