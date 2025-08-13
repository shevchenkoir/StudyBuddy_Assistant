# # app/main.py
# from pathlib import Path
# import os
# import sys
# import subprocess
# import shutil
# import time

# # --- 1) Пути проекта ---
# ROOT = Path(__file__).resolve().parents[1]          # корень репо
# GUI_APP = ROOT / "gui" / "streamlit_app.py"         # streamlit-приложение
# CHECKER = ROOT / "check_ollama_connection.py"       # проверка Ollama

# # чтобы import работал из корня
# if str(ROOT) not in sys.path:
#     sys.path.insert(0, str(ROOT))


# try:
#     from dotenv import load_dotenv
#     load_dotenv(ROOT / ".env")
# except Exception:
#     pass  # если dotenv не установлен — просто идём дальше

# def run_checker():
#     """
#     Пытаемся импортировать функцию из check_ollama_connection.py.
#     Если её нет, просто запускаем файл как скрипт.
#     """
#     if not CHECKER.exists():
#         print("⚠️ Не найден check_ollama_connection.py — пропускаю проверку Ollama.")
#         return

#     print("🔎 Проверяю Ollama и модели…")
#     try:
#         # Попробуем вызвать как модуль с функцией ensure_ollama_ready()
#         import importlib.util
#         spec = importlib.util.spec_from_file_location("ollama_checker", str(CHECKER))
#         mod = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(mod)  # type: ignore

#         if hasattr(mod, "ensure_ollama_ready"):
#             mod.ensure_ollama_ready()
#         elif hasattr(mod, "main"):
#             mod.main()
#         else:
#             # Фоллбек — просто запустим скрипт отдельным процессом
#             subprocess.run([sys.executable, str(CHECKER)], check=True)
#     except Exception as e:
#         print(f"⚠️ Не удалось выполнить проверку Ollama: {e}")
#     else:
#         print("✅ Ollama готова.")

# def run_streamlit():
#     """
#     Запуск Streamlit-приложения.
#     """
#     # Проверим, установлен ли streamlit
#     streamlit_bin = shutil.which("streamlit")
#     if streamlit_bin is None:
#         # возможно в виртуалке: python -m streamlit ...
#         cmd = [sys.executable, "-m", "streamlit", "run", str(GUI_APP)]
#     else:
#         cmd = [streamlit_bin, "run", str(GUI_APP)]

#     # Полезно явно пробросить адрес Ollama из .env, если он есть
#     env = os.environ.copy()
#     env.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")

#     print(f"🌐 Стартую Streamlit: {GUI_APP}")
#     time.sleep(0.2)
#     subprocess.run(cmd, env=env, check=True)

# if __name__ == "__main__":
#     # 1) проверка и автоподнятие Ollama + модели
#     run_checker()
#     # 2) запуск веб-приложения
#     run_streamlit()
# app/main.py
from pathlib import Path
import os
import sys
import subprocess
import time

# --- Пути ---
ROOT = Path(__file__).resolve().parents[1]
GUI_APP = ROOT / "gui" / "streamlit_app.py"
CHECKER = ROOT / "check_ollama_connection.py"

# Импорт из корня
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# --- .env ---
try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except Exception:
    pass

def run_checker(no_interactive=True):
    """
    Выполняет проверку Ollama и моделей из check_ollama_connection.py,
    при этом отключает открытие отдельного окна с `ollama run ...`.
    """
    if not CHECKER.exists():
        print("⚠️ Не найден check_ollama_connection.py — пропускаю проверку Ollama.")
        return

    print("🔎 Проверяю Ollama и модели…")
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("ollama_checker", str(CHECKER))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore

        # жестко отключаем интерактивный run, чтобы не плодить окна
        if no_interactive and hasattr(mod, "AUTO_OPEN_INTERACTIVE_RUN"):
            mod.AUTO_OPEN_INTERACTIVE_RUN = False
        if no_interactive and hasattr(mod, "open_interactive_run"):
            # перестраховка: на случай прямого вызова
            mod.open_interactive_run = lambda *a, **kw: None  # type: ignore

        # вызываем основную функцию
        if hasattr(mod, "ensure_ollama_ready"):
            mod.ensure_ollama_ready()   # если есть такая
        elif hasattr(mod, "main"):
            mod.main()                  # иначе обычный main
        else:
            # Фоллбек: запустить как скрипт в том же окне
            subprocess.run([sys.executable, str(CHECKER)], check=False)
    except Exception as e:
        print(f"⚠️ Не удалось выполнить проверку Ollama: {e}")
    else:
        print("✅ Ollama готова.")

def run_streamlit():
    """
    Запускаем Streamlit через python -m streamlit (без streamlit.EXE),
    чтобы не ловить Windows launcher error.
    """
    env = os.environ.copy()
    env.setdefault("OLLAMA_BASE_URL", "http://localhost:11434")
    cmd = [sys.executable, "-m", "streamlit", "run", str(GUI_APP)]

    print(f"🌐 Стартую Streamlit: {GUI_APP}")
    time.sleep(0.2)
    # check=False — чтобы видеть ошибку в консоли streamlit, а не падать здесь
    subprocess.run(cmd, env=env, check=False)

if __name__ == "__main__":
    # 1) Проверка и автоподнятие Ollama + моделей (без лишних окон)
    run_checker(no_interactive=True)
    # 2) Запуск веб-приложения в этом же терминале
    run_streamlit()
