import telebot
from config import TOKEN, CHANNEL_USERNAME
from utils import send_welcome, handle_hikka_button

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    send_welcome(bot, message.chat.id, CHANNEL_USERNAME)

@bot.message_handler(func=lambda message: message.text == "Hikka-Telethon")
def hikka_button_pressed(message):
    handle_hikka_button(bot, message.chat.id)

if __name__ == '__main__':
    bot.polling()
