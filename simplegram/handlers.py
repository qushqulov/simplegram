from .types import Update
from .bot import Bot
from .filters import Filters


class Handler:
    def check_update(self, update: Update) -> bool:
        raise NotImplementedError

    def handle_update(self, update: Update, bot: Bot):
        raise NotImplementedError

 
class CommandHandler(Handler):
    def __init__(self, command: str, callback):
        self.command = command
        self.callback = callback

    def check_update(self, update: Update) -> bool:
        if not update.message or not update.message.text:
            return False
        else:
            return update.message.text.startswith(f"/{self.command}")

    def handle_update(self, update: Update, bot: Bot):
        self.callback(update, bot)


class MessageHandler:
    def __init__(self, filters: Filters, callback):
        self.filters = filters
        self.callback = callback

    def check_update(self, update: Update) -> bool:
        if not update.message:
            return False
        else:
            return self.filters(update.message)

    def handle_update(self, update: Update, bot: Bot):
        self.callback(update, bot)
