from .types import Message


class Filters:
    @staticmethod
    def text(message: Message) -> bool:
        return message.text is not None

    @staticmethod
    def photo(message: Message) -> bool:
        return message.photo is not None

    @staticmethod
    def location(message: Message) -> bool:
        return message.location is not None
 