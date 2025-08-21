# import pyttsx3
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Получаем скорость речи из .env
# TTS_RATE = int(os.getenv("TTS_RATE", 175))

# # Инициализируем движок TTS
# engine = pyttsx3.init()
# engine.setProperty('rate', TTS_RATE)  # скорость речи
# engine.setProperty('volume', 1.0)     # громкость (0.0–1.0)

# def speak(text: str):
#     print(f"🗣 говорит: {text}")
#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as e:
#         print(f"❌ Ошибка синтеза речи: {e}")

# output/speech_output.py
"""
Надёжная озвучка для Streamlit/Windows:
- РЕЖИМ ПО УМОЛЧАНИЮ: spawn-per-call  → новый движок на каждый вызов speak()
- Без очередей и фоновых тредов → нечему падать между реранами
- Лог каждой озвучки в терминал

Если захочешь вернуть прежний режим (постоянный воркер с очередью),
установи переменную окружения TTS_MODE=persist (но spawn стабильнее).
"""

from __future__ import annotations
import os
import threading
import time
import pyttsx3

_RATE = int(os.getenv("TTS_RATE", os.getenv("SPEECH_RATE", "175")))
_VOLUME = float(os.getenv("TTS_VOLUME", "1.0"))
_VOICE  = os.getenv("TTS_VOICE", "")
_MODE   = os.getenv("TTS_MODE", "spawn").lower().strip()  # 'spawn' | 'persist'

# ---------- SPAWN-PER-CALL ----------
def _speak_spawn(text: str):
    print(f"[TTS-SPAWN] {text}")
    try:
        eng = pyttsx3.init(driverName="sapi5")  # явно SAPI5 на Windows
        eng.setProperty("rate", _RATE)
        eng.setProperty("volume", _VOLUME)
        if _VOICE:
            try:
                voices = eng.getProperty("voices")
                match = next(
                    (v for v in voices
                     if _VOICE.lower() in (v.name or "").lower()
                     or _VOICE.lower() in (v.id or "").lower()),
                    None
                )
                if match:
                    eng.setProperty("voice", match.id)
            except Exception:
                pass
        eng.say(text)
        eng.runAndWait()
        # Важно корректно закрывать
        try:
            eng.stop()
        except Exception:
            pass
    except Exception as e:
        print(f"[TTS-SPAWN:ERROR] {e}")

# ---------- PERSISTENT MODE (опционально) ----------
# Оставлю на случай, если захочешь вернуться:
import queue
import threading
_engine = None
_queue = queue.Queue()
_worker = None
_started = False

def _init_engine_if_needed():
    global _engine
    if _engine is None:
        eng = pyttsx3.init(driverName="sapi5")
        eng.setProperty("rate", _RATE)
        eng.setProperty("volume", _VOLUME)
        if _VOICE:
            try:
                voices = eng.getProperty("voices")
                match = next((v for v in voices if _VOICE.lower() in (v.name or "").lower()
                              or _VOICE.lower() in (v.id or "").lower()), None)
                if match:
                    eng.setProperty("voice", match.id)
            except Exception:
                pass
        _engine = eng

def _worker_loop():
    while True:
        item = _queue.get()
        if item is None:
            break
        text = (item or "").strip()
        try:
            if text:
                print(f"[TTS] {text}")
                _engine.say(text)
                _engine.runAndWait()
        except Exception as e:
            print(f"[TTS:ERROR] {e}")
        finally:
            _queue.task_done()
    try:
        _engine.stop()
    except Exception:
        pass

def ensure_started():
    """Для persist-режима: безопасный старт воркера (игнорируется в spawn)."""
    global _worker, _started
    if _MODE != "persist":
        return
    if not _started:
        _init_engine_if_needed()
        _worker = threading.Thread(target=_worker_loop, name="TTSWorker", daemon=True)
        _worker.start()
        _started = True

# ---------- ПУБЛИЧНАЯ ФУНКЦИЯ ----------
def speak(text: str, flush: bool = False, debounce_sec: float = 0.0):
    """Кроссплатформенная обёртка. По умолчанию использует spawn-per-call."""
    if not isinstance(text, str):
        text = str(text)

    # простая защита от дребезга
    if debounce_sec > 0:
        now = time.monotonic()
        last = getattr(speak, "_last_time", 0.0)
        last_txt = getattr(speak, "_last_text", "")
        if text == last_txt and (now - last) < debounce_sec:
            return
        speak._last_time = now
        speak._last_text = text

    if _MODE == "persist":
        ensure_started()
        if flush:
            try:
                while True:
                    _queue.get_nowait()
                    _queue.task_done()
            except queue.Empty:
                pass
        _queue.put(text)
    else:
        # SPAWN сразу в отдельном лёгком потоке, чтобы не блокировать UI
        threading.Thread(target=_speak_spawn, args=(text,), daemon=True).start()

def shutdown():
    """Корректное завершение persist-режима (spawn этого не требует)."""
    if _MODE == "persist":
        try:
            _queue.put(None)
            _queue.join()
        except Exception:
            pass

