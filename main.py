import os

from dotenv import load_dotenv

from simplegram import Updater


load_dotenv()

updater = Updater(os.getenv("TOKEN"))
updater.start_polling()
