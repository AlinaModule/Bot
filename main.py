import telebot
from config import TOKEN, CHANNEL_USERNAME
from utils import send_welcome, send_start_menu, create_back_button, author_info

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    send_welcome(bot, message.chat.id, CHANNEL_USERNAME)
    send_start_menu(bot, message.chat.id)

@bot.message_handler(commands=['botinfo'])
def o_bote_command(message):
    o_bote(bot, message.chat.id)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    chat_id = message.chat.id
    text = message.text

    try:
        chat_member = bot.get_chat_member(CHANNEL_USERNAME, chat_id)
        if chat_member.status not in ['member', 'administrator', 'creator']:
            send_welcome(bot, chat_id, CHANNEL_USERNAME)
            return
    except Exception as e:
        print(f'Ошибка при проверке подписки: {e}')
        
    if text in ["Hikka-Telethon", "RimTUB-Pyrogram", "Pyrogram", "Telethon", "Telebot"]:
        if text == "Hikka-Telethon":
            article_text = "🎆 <b>Статья:</b> <a href='https://telegra.ph/Telethon-pro-moduli-dlya-Hikka-10-30'>[Telethon-про модули для Hikka]</a>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        elif text == "RimTUB-Pyrogram":
            article_text = "💉 <b>Статья:</b> <a href='https://telegra.ph/Pyrogram-pro-moduli-dlya-RimTUB-10-30'>[RimTUB-про то как написать для него модуль]</a>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        elif text == "Pyrogram":
            article_text = "📀 <b>Статья:</b> <a href='https://telegra.ph/Pyrogram-razrabotka-bota-10-30'>[Pyrogram-про то как написать простого телеграм бота]</a>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        elif text == "Telethon":
            article_text = "⚙️ <b>Статья:</b> <a href='https://telegra.ph/Telethon-kak-napisat-svoego-telegram-bota-10-30'>[Telethon-про то как написать тг-бота]</a>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        elif text == "Telebot":
            article_text = "✨ <b>Статья:</b> <a href'https://telegra.ph/Telebot-razrabotka-bota-10-30'>[Telebot-о том как написать простого телеграм бота]</a>"
            bot.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())

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
