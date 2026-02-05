import os

from dotenv import load_dotenv

from simplegram import Bot


load_dotenv()


bot = Bot(os.getenv("TOKEN"))

for update in bot.get_updates():
    print(update.update_id)
