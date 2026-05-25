"""
AI Telegram Motivation Bot
"""

import os
import requests

from dotenv import load_dotenv
from openai import OpenAI



load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENAI_API_KEY,
)
from datetime import datetime, timedelta

IST = datetime.utcnow() + timedelta(hours=5, minutes=30)
now = IST.strftime('%Y-%m-%d %H:%M IST')


with open("context.txt", "r") as file:
    context = file.read()


prompt = f"""
{context}

Generate ONE powerful evening Telegram message.this is the time so send it accordingly {now}

Style:
- personal
- emotionally intelligent
- ambitious
- slightly romantic/warm , give more focus on it .
- intense
- deeply motivating
- human
- a quote that is romentic and motivating


Keep under 20 words.
Keep it under 20 Words ..
Keep it under 20 Words .. 
i Reapat , Keep it under 20 words..

Add emojis naturally.
"""


response = client.chat.completions.create(
    model="openai/gpt-oss-120b:free",
    messages=[
        {
            "role": "system",
            "content": prompt
        }
    ]
)


message = response.choices[0].message.content


telegram_url = (
    f"https://api.telegram.org/bot"
    f"{TELEGRAM_BOT_TOKEN}/sendMessage"
)


payload = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": message
}


requests.post(
    telegram_url,
    json=payload
)


