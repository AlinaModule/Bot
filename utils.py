import telebot

def send_welcome(bot, chat_id, channel_username):
    """Отправляет приветственное сообщение после проверки подписки."""
    try:
        chat_member = bot.get_chat_member(channel_username, chat_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            bot.send_message(
                chat_id,
                "✨ <b>Приветствую тебя в этом боте!</b>\n\n<b>С помощью него ты сможешь написать самого простого телеграм бота или модуль для какого-либо юзербота, не отрицаю что скоро в боте будет ещё много новых функций, но перед тем как ты познакомишься с материалами подпишись на мой канальчик по кнопке ниже ♡</b>"
            )
    except Exception as e:
        print(f'Ошибка при проверке подписки: {e}')


def send_start_menu(bot, chat_id):
    """Отправляет стартовое меню с кнопками выбора категории."""
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    userbots_button = telebot.types.KeyboardButton("Юзерботы")
    tg_bots_button = telebot.types.KeyboardButton("ТГ-боты")

    keyboard.add(userbots_button, tg_bots_button)

    bot.send_message(chat_id, "💫 <b>Выберите направление:</b>", reply_markup=keyboard)

def create_back_button():
    """Создает клавиатуру с одной кнопкой 'Назад'"""
    back_button = telebot.types.KeyboardButton('Назад')
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(back_button)
    return keyboard

if __name__ == "__main__":
    bot.polling(none_stop=True)
