# SimpleGram

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Oddiy va sync Telegram bot kutubxonasi. Python-telegram-bot kabi murakkab emas, lekin barcha asosiy funksiyalar mavjud.

## ✨ Xususiyatlar

- ✅ Sync (asinxron emas) - oddiy va tushunarli
- ✅ Minimal kod - ortiqcha murakkablik yo'q
- ✅ Oson o'rganish - yangi boshlovchilar uchun qulay
- ✅ Handler tizimi - CommandHandler, MessageHandler
- ✅ Filter tizimi - text, photo, command
- ✅ Type hinting - kod o'qish oson

## 📦 O'rnatish

```bash
# Repository ni clone qiling
git clone https://github.com/nt-sn04/simplegram.git
cd simplegram

# Dependencies o'rnating
pip install -r requirements.txt
```

## 🚀 Tezkor Boshlash

### Oddiy Echo Bot

```python
from simplegram import Updater, CommandHandler, MessageHandler, Filters

def start(message):
    updater.bot.send_message(message.chat.id, "Salom! Men echo botman.")

def echo(message):
    updater.bot.send_message(message.chat.id, message.text)

updater = Updater('YOUR_BOT_TOKEN')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(echo, filters=Filters.text))
updater.start_polling()
```

### Ko'proq Misollar

#### Komandalar bilan ishlash

```python
from simplegram import Updater, CommandHandler

def start(message):
    updater.bot.send_message(message.chat.id, "👋 Salom!")

def help_command(message):
    text = """
📚 Yordam:
/start - Botni ishga tushirish
/help - Yordam ko'rish
/about - Bot haqida
    """
    updater.bot.send_message(message.chat.id, text)

def about(message):
    updater.bot.send_message(message.chat.id, "SimpleGram kutubxonasi bilan yaratilgan")

updater = Updater('YOUR_BOT_TOKEN')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('about', about))
updater.start_polling()
```

#### Rasm bilan ishlash

```python
from simplegram import Updater, MessageHandler, Filters

def handle_photo(message):
    updater.bot.send_message(message.chat.id, "📸 Rasm qabul qilindi!")

def handle_text(message):
    updater.bot.send_message(message.chat.id, f"Siz yozdingiz: {message.text}")

updater = Updater('YOUR_BOT_TOKEN')
updater.dispatcher.add_handler(MessageHandler(handle_photo, filters=Filters.photo))
updater.dispatcher.add_handler(MessageHandler(handle_text, filters=Filters.text))
updater.start_polling()
```

#### Rasm yuborish

```python
from simplegram import Updater, CommandHandler

def send_cat(message):
    # URL orqali
    updater.bot.send_photo(
        message.chat.id, 
        'https://cataas.com/cat',
        caption='🐱 Mushuk rasmi'
    )
    
    # Fayl orqali
    # updater.bot.send_photo(message.chat.id, 'cat.jpg', caption='Mushuk')

updater = Updater('YOUR_BOT_TOKEN')
updater.dispatcher.add_handler(CommandHandler('cat', send_cat))
updater.start_polling()
```

## 📚 Hujjatlar

### Asosiy Klasslar

#### Updater
```python
updater = Updater('TOKEN')
updater.start_polling(interval=1)  # interval - update olish oralig'i (sekund)
updater.stop()  # Botni to'xtatish
```

#### Bot
```python
bot = updater.bot
bot.send_message(chat_id, text)
bot.send_photo(chat_id, photo, caption=None)
bot.get_me()  # Bot haqida ma'lumot
```

#### Handlers

**CommandHandler** - Komandalarni ushlash
```python
CommandHandler('start', callback_function)
```

**MessageHandler** - Xabarlarni ushlash
```python
MessageHandler(callback_function, filters=Filters.text)
```

#### Filters

```python
Filters.text      # Matn xabarlari
Filters.photo     # Rasm xabarlari
Filters.command   # Komandalar
```

#### Types

```python
# Message
message.text          # Xabar matni
message.chat.id       # Chat ID
message.from_user.id  # Foydalanuvchi ID
message.photo         # Rasm
message.document      # Hujjat

# Update
update.message        # Message obyekti
update.update_id      # Update ID
```

## 📁 Loyiha Strukturasi

```
simplegram/
├── simplegram/
│   ├── __init__.py       # Package exports
│   ├── bot.py            # Bot API metodlari
│   ├── updater.py        # Update olish va polling
│   ├── dispatcher.py     # Handler boshqaruvi
│   ├── handlers.py       # Handler va Filter klasslar
│   └── types.py          # Type klasslar (User, Chat, Message, Update)
├── examples/
│   ├── echo_bot.py
│   ├── command_bot.py
│   └── photo_bot.py
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 🔧 Talablar

- Python 3.10+
- requests

## 🤝 Hissa Qo'shish

Pull request'lar xush kelibsiz! Katta o'zgarishlar uchun avval issue oching.

1. Fork qiling
2. Feature branch yarating (`git checkout -b feature/AmazingFeature`)
3. O'zgarishlarni commit qiling (`git commit -m 'Add some AmazingFeature'`)
4. Branch'ni push qiling (`git push origin feature/AmazingFeature`)
5. Pull Request oching

## 📝 Litsenziya

MIT License - [LICENSE](LICENSE) faylga qarang

## 🙏 Credits

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Ilhom manbai

## 📞 Aloqa

Muammolar yoki savollar bo'lsa [Issues](https://github.com/nt-sn04/simplegram/issues) bo'limida yozing.

---

⭐ Agar loyiha yoqsa, repository'ga star bering!
