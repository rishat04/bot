import telebot
import os
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
WEBAPP_URL = 'https://kgasu.onrender.com'

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        text="Открыть приложение", 
        web_app=WebAppInfo(url=WEBAPP_URL)
    ))
    bot.send_message(
        message.chat.id,"Привет, Первокурсник! Добро пожаловать в КГАСУ. Твоя задача — пройти 5 станций, чтобы стать настоящим студентом нашего универа. Готов? Погнали!",
        reply_markup=markup
    )

# Запускаем бота
bot.polling()