import telebot
from telebot import types

def create_subscription_keyboard():
    """Создает клавиатуру с кнопкой "Подписаться на канал"."""
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подписаться на канал", url=f"https://t.me/{config.CHANNEL_ID}")
    keyboard.add(url_button)
    return keyboard