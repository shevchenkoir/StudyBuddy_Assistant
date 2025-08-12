import os
import sys
from telegram.ext import Updater, MessageHandler, Filters

# Add root directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.rag_engine import get_answer

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "PASTE-YOUR-TOKEN-HERE")

def handle_message(update, context):
    user_message = update.message.text
    update.message.reply_text("🤖 Думаю над ответом...")
    answer = get_answer(user_message)
    update.message.reply_text(f"📘 Ответ:\n{answer}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()