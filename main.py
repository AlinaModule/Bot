import telebot
from config import TOKEN, CHANNEL_USERNAME
from utils import send_welcome

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    send_welcome(bot, message.chat.id, CHANNEL_USERNAME)

if __name__ == '__main__':
    bot.polling()
