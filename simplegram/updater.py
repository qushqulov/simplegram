import time

from .bot import Bot


class Updater:
    def __init__(self, token: str):
        self.token = token
        self.bot = Bot(self.token)
        self.offset = None
        self.running = False

    def start_polling(self, interval: int = 1):
        self.running = True

        while self.running:
            updates = self.bot.get_updates(offset=self.offset)

            for update in updates:
                print(update.update_id)

                self.offset = update.update_id + 1

            time.sleep(interval)

    def stop(self):
        self.running = False
