import requests
from src.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_message(text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, json=payload)
    return "Telegram message sent"
