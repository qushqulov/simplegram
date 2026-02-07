import os

from dotenv import load_dotenv

from simplegram import (
    Updater,
    Update,
    Bot,
    Filters,
    CommandHandler,
    MessageHandler,
)


load_dotenv()


def start(update: Update, bot: Bot):
    bot.send_message(chat_id=update.message.chat.id, text="Salom botga xush kelibsiz!")


def help(update: Update, bot: Bot):
    bot.send_message(chat_id=update.message.chat.id, text="Qanday yordam bera olaman?")


def echo(update: Update, bot: Bot):
    bot.send_message(chat_id=update.message.chat.id, text=update.message.text)


updater = Updater(os.getenv("TOKEN"))

updater.dispatcher.add_handler(CommandHandler(command="start", callback=start))
updater.dispatcher.add_handler(CommandHandler(command="help", callback=help))

updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=echo))

<<<<<<< HEAD
updater.start_polling()
 
=======
updater.start_polling()
>>>>>>> 9bbc34a7851523d93cf5418cd8e3cf6ad7e7d39b
