import telebot
from config import TOKEN, CHANNEL_USERNAME
from utils import (
    send_welcome,
    handle_hikka_button,
    send_start_menu,
    handle_userbots,
    handle_tgbots,
    handle_rimtub_button,
    handle_pyrogram_button,
    handle_telethon_button,
    handle_telebot_button
)

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def start_command(message):
    send_welcome(bot, message.chat.id, CHANNEL_USERNAME)

# Обработчик нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    chat_id = message.chat.id
    text = message.text
    
    if text == "Юзерботы":
        handle_userbots(bot, chat_id)
    elif text == "Hikka-Telethon":
        handle_hikka_button(bot, chat_id)
    elif text == "RimTUB-Pyrogram":
        handle_rimtub_button(bot, chat_id)
    
    if text == "ТГ-боты":
        handle_tgbots(bot, chat_id)
    elif text == "Pyrogram":
        handle_pyrogram_button(bot, chat_id)
    elif text == "Telethon":
        handle_telethon_button(bot, chat_id)
    elif text == "Telebot":
        handle_telebot_button(bot, chat_id)
        
if __name__ == '__main__':
    bot.polling(none_stop=True)
