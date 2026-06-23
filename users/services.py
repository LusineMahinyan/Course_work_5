import requests
from django.conf import settings


def send_telegram_message(chat_id: str, message: str):
    """
    Отправка сообщения в Telegram
    """

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message,
    }

    response = requests.post(url, data=data)

    return response.json()
