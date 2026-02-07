from .types import Update
from .handlers import Handler
from .bot import Bot


class Dispatcher:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.handlers: list[Handler] = []

    def add_handler(self, handler):
        if handler not in self.handlers:
            self.handlers.append(handler)

    def process_update(self, update: Update):
        for handler in self.handlers:
            if handler.check_update(update):
                handler.handle_update(update, self.bot)
                break
 