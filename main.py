import telebot
from config import TOKEN, CHANNEL_USERNAME
from utils import send_welcome, send_start_menu, create_back_button

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    send_welcome(bot, message.chat.id, CHANNEL_USERNAME)
    send_start_menu(bot, message.chat.id)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    chat_id = message.chat.id
    text = message.text

    if text in ["Hikka-Telethon", "RimTUB-Pyrogram", "Pyrogram", "Telethon", "Telebot"]:
        if text == "Hikka-Telethon":
            article_text = "🎆 **Статья:** <[Telethon-про модули для Hikka](https://telegra.ph/Telethon-pro-moduli-dlya-Hikka-10-30)>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="Markdown", reply_markup=create_back_button())
        elif text == "RimTUB-Pyrogram":
            article_text = "💉 **Статья:** <[RimTUB-про то как написать для него модуль](https://telegra.ph/Pyrogram-pro-moduli-dlya-RimTUB-10-30)>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="Markdown", reply_markup=create_back_button())
        elif text == "Pyrogram":
            article_text = "📀 **Статья:** <[Pyrogram-про то как написать простого телеграм бота](https://telegra.ph/Pyrogram-razrabotka-bota-10-30)>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="Markdown", reply_markup=create_back_button())
        elif text == "Telethon":
            article_text = "⚙️ **Статья:** <[Telethon-про то как написать тг-бота](https://telegra.ph/Telethon-kak-napisat-svoego-telegram-bota-10-30)>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="Markdown", reply_markup=create_back_button())
        elif text == "Telebot":
            article_text = "✨ **Статья:** <[Telebot-о том как написать простого телеграм бота](https://telegra.ph/Telebot-razrabotka-bota-10-30)>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="Markdown", reply_markup=create_back_button())

    elif text == "Юзерботы":
        hikka_telethon_button = telebot.types.KeyboardButton("Hikka-Telethon")
        rimtub_pyrogram_button = telebot.types.KeyboardButton("RimTUB-Pyrogram")
        back_button = telebot.types.KeyboardButton('Назад')
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row(hikka_telethon_button, rimtub_pyrogram_button)  # Изменено: Hikka-Telethon перед RimTUB-Pyrogram
        keyboard.add(back_button)
        bot.send_message(chat_id, "🖥️ <b>Выберите юзербота и библиотеку:</b>",
                         reply_markup=keyboard, parse_mode='HTML')

    elif text == "ТГ-боты":
        pyrogram_tgbots_button = telebot.types.KeyboardButton("Pyrogram")
        telethon_tgbots_button = telebot.types.KeyboardButton("Telethon")
        telebot_tgbots_button = telebot.types.KeyboardButton("Telebot")
        back_button = telebot.types.KeyboardButton('Назад')
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row(telethon_tgbots_button, pyrogram_tgbots_button, telebot_tgbots_button)  # Изменено: порядок кнопок
        keyboard.add(back_button)
        bot.send_message(chat_id, "📚 <b>Выберите библиотеку для написания бота:</b>",
                         reply_markup=keyboard, parse_mode='HTML')

    else:
        send_start_menu(bot, message.chat.id)

bot.polling(none_stop=True)
