from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    bot_token: str = os.getenv("BOT_TOKEN", "")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    llm_base_url: str = os.getenv("LLM_BASE_URL", "http://localhost:11434")
    llm_model: str = os.getenv("LLM_MODEL", "qwen2.5:1.5b-instruct")
    tesseract_cmd: str = os.getenv("TESSERACT_CMD", "")

settings = Settings()
