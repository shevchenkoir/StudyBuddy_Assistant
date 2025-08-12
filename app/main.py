# app/main.py
from pathlib import Path
import os
import sys
import subprocess
import shutil
import time

# --- 1) Пути проекта ---
ROOT = Path(__file__).resolve().parents[1]          # корень репо
GUI_APP = ROOT / "gui" / "streamlit_app.py"         # streamlit-приложение
CHECKER = ROOT / "check_ollama_connection.py"       # проверка Ollama

# чтобы import работал из корня
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except Exception:
    pass  # если dotenv не установлен — просто идём дальше

def run_checker():
    """
    Пытаемся импортировать функцию из check_ollama_connection.py.
    Если её нет, просто запускаем файл как скрипт.
    """
    if not CHECKER.exists():
        print("⚠️ Не найден check_ollama_connection.py — пропускаю проверку Ollama.")
        return

    print("🔎 Проверяю Ollama и модели…")
    try:
        # Попробуем вызвать как модуль с функцией ensure_ollama_ready()
        import importlib.util
        spec = importlib.util.spec_from_file_location("ollama_checker", str(CHECKER))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore

        if hasattr(mod, "ensure_ollama_ready"):
            mod.ensure_ollama_ready()
        elif hasattr(mod, "main"):
            mod.main()
        else:
            # Фоллбек — просто запустим скрипт отдельным процессом
            subprocess.run([sys.executable, str(CHECKER)], check=True)
    except Exception as e:
        print(f"⚠️ Не удалось выполнить проверку Ollama: {e}")
    else:
        print("✅ Ollama готова.")

def run_streamlit():
    """
    Запуск Streamlit-приложения.
    """
    # Проверим, установлен ли streamlit
    streamlit_bin = shutil.which("streamlit")
    if streamlit_bin is None:
        # возможно в виртуалке: python -m streamlit ...
        cmd = [sys.executable, "-m", "streamlit", "run", str(GUI_APP)]
    else:
        cmd = [streamlit_bin, "run", str(GUI_APP)]

    # Полезно явно пробросить адрес Ollama из .env, если он есть
    env = os.environ.copy()
    env.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")

    print(f"🌐 Стартую Streamlit: {GUI_APP}")
    time.sleep(0.2)
    subprocess.run(cmd, env=env, check=True)

if __name__ == "__main__":
    # 1) проверка и автоподнятие Ollama + модели
    run_checker()
    # 2) запуск веб-приложения
    run_streamlit()
