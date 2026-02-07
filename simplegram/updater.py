import time

from .bot import Bot
from .dispatcher import Dispatcher


class Updater:
    def __init__(self, token: str):
        self.token = token
        self.bot = Bot(self.token)
        self.dispatcher = Dispatcher(self.bot) 
        self.offset = None
        self.running = False

    def start_polling(self, interval: int = 1):
        self.running = True

        while self.running:
            updates = self.bot.get_updates(offset=self.offset)

            for update in updates:
                self.dispatcher.process_update(update)

                self.offset = update.update_id + 1

            time.sleep(interval)

    def stop(self):
        self.running = False
