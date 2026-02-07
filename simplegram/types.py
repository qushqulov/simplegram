class User:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data.get("last_name")
        self.username = data.get("username")


class Chat:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.type = data["type"]


class Message:
    def __init__(self, data: dict):
        self.message_id = data["message_id"]
        self.from_user = User(data["from"]) if data.get("from") else None
        self.chat = Chat(data["chat"]) if data.get("chat") else None
        self.text: str = data.get("text")
        self.photo: dict = data.get("photo")
        self.location: dict = data.get("location")


class Update:
    def __init__(self, data: dict):
        self.update_id = data["update_id"]
        self.message = Message(data["message"]) if data.get("message") else None
 