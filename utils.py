import telebot

def send_welcome(bot, chat_id, channel_username):
    """Отправляет приветственное сообщение после проверки подписки."""
    try:
        chat_member = bot.get_chat_member(channel_username, chat_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            bot.send_message(
                chat_id,
                "Благодарим за подписку на канал, для работы с ботом используйте команды в специальном списке."
            )
    except Exception as e:
        print(f'Ошибка при проверке подписки: {e}')


def send_start_menu(bot, chat_id):
    """Отправляет стартовое меню с кнопками выбора категории."""
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    userbots_button = telebot.types.KeyboardButton("Юзерботы")
    tg_bots_button = telebot.types.KeyboardButton("ТГ-боты")

    keyboard.add(userbots_button, tg_bots_button)

    bot.send_message(chat_id, "Выберите категорию:", reply_markup=keyboard)

if __name__ == "__main__":
    bot.polling(none_stop=True)
