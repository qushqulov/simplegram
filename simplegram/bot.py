import requests

from .types import Update


class Bot:
    def __init__(self, token: str):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{self.token}"

    def send_message(self, chat_id: str | int, text: str):
        data = {
            "chat_id": chat_id,
            "text": text,
        }
        response = requests.post(
            f"{self.base_url}/sendMessage",
            data=data,
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Telegram xatolik qaytardi!")

    def get_updates(
        self, offset: int | None = None, limit: int = 20, timeout: int = 30
    ) -> list[Update]:
        payload = {
            "offset": offset,
            "limit": limit,
            "timeout": timeout,
        }
        response = requests.get(f"{self.base_url}/getUpdates", params=payload)

        if response.status_code == 200:
            updates = []
            for update_data in response.json()["result"]:
                updates.append(Update(update_data))

            return updates
        else:
            raise Exception("Telegram xatolik qaytardi!")
