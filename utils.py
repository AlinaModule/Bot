import telebot

def send_welcome(bot, chat_id, channel_username):
    chat_member = bot.get_chat_member(channel_username, chat_id)
    
    if chat_member.status in ['member', 'administrator', 'creator']:
        bot.send_message(chat_id, 
                         "Благодарим за подписку на канал, для работы с ботом используйте команды в специальном списке.")
    else:
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton("Перейти к каналу", url=f"https://t.me/{channel_username[1:]}")
        markup.add(button)

        bot.send_message(chat_id, 
                         "Для работы с ботом подпишитесь на канал ниже:", 
                         reply_markup=markup)
