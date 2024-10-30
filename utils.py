import telebot

def send_welcome(bot, chat_id, channel_username):
    try:
        chat_member = bot.get_chat_member(channel_username, chat_id)
        
        if chat_member.status in ['member', 'administrator', 'creator']:
            bot.send_message(chat_id, 
                             "Благодарим за подписку на канал, для работы с ботом используйте команды в специальном списке.")
            send_keyboard(bot, chat_id)  # Отправляем клавиатуру после подписки
        else:
            markup = telebot.types.InlineKeyboardMarkup()
            button = telebot.types.InlineKeyboardButton("Перейти к каналу", url=f"https://t.me/{channel_username[1:]}")
            markup.add(button)

            bot.send_message(chat_id, 
                             "Для работы с ботом подпишитесь на канал ниже:", 
                             reply_markup=markup)
    except Exception as e:
        bot.send_message(chat_id, "Произошла ошибка при проверки подписки.")
        print(f"Error: {e}")

def send_keyboard(bot, chat_id):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_hikka = telebot.types.KeyboardButton("Hikka-Telethon")
    keyboard.add(button_hikka)
    bot.send_message(chat_id, "Нажмите кнопку:", reply_markup=keyboard)

def handle_hikka_button(bot, chat_id):
    text = "Статья: [Telethon-про модули для Hikka](https://telegra.ph/Telethon-pro-moduli-dlya-Hikka-10-30)"
    bot.send_message(
        chat_id,
        text,
        disable_web_page_preview=True,
        parse_mode='Markdown'
            )
