from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import TOKEN, CHANNEL_USERNAME
from utils import send_welcome, o_bote, send_start_menu, create_back_button

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Form(StatesGroup):
  name = State()
  age = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
  await send_welcome(bot, message.chat.id, CHANNEL_USERNAME)
  await send_start_menu(bot, message.chat.id)

@dp.message_handler(commands=['botinfo'])
async def cmd_botinfo(message: types.Message):
  try:
    chat_member = await bot.get_chat_member(CHANNEL_USERNAME, message.chat.id)
    if chat_member.status not in ['member', 'administrator', 'creator']:
      await send_welcome(bot, message.chat.id, CHANNEL_USERNAME)
      return
  except Exception as e:
    print(f'error: {e}')
  await o_bote(bot, message.chat.id)

@dp.message_handler(regexp=r"^\.(.*)")
async def handle_alias(message: types.Message):
  command = message.text[1:]
  if command == "старт":
    await cmd_start(message)
  elif command == "ботинфо":
    await cmd_botinfo(message)
  else:
    await message.reply("Неизвестная команда.")

@dp.callback_query_handler(lambda c: c.data == 'back')
async def process_callback_back(callback_query: types.CallbackQuery):
  await callback_query.message.edit_text("💫 Выберите направление:", reply_markup=send_start_menu(bot, callback_query.message.chat.id), parse_mode='HTML')
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Hikka-Telethon')
async def process_callback_hikka(callback_query: types.CallbackQuery):
  article_text = "🎆 Статья: [Telethon-про модули для Hikka]"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'RimTUB-Pyrogram')
async def process_callback_rimtub(callback_query: types.CallbackQuery):
  article_text = "💉 <b>Статья:</b> <a href='https://telegra.ph/Pyrogram-pro-moduli-dlya-RimTUB-10-30'>[RimTUB-про то как написать для него модуль]</a>"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Pyrogram')
async def process_callback_pyrogram(callback_query: types.CallbackQuery):
  article_text = "📀 <b>Статья:</b> <a href='https://telegra.ph/Pyrogram-razrabotka-bota-10-30'>[Pyrogram-про то как написать простого телеграм бота]</a>"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Telethon')
async def process_callback_telethon(callback_query: types.CallbackQuery):
  article_text = "⚙️ <b>Статья:</b> <a href='https://telegra.ph/Telethon-kak-napisat-svoego-telegram-bota-10-30'>[Telethon-про то как написать тг-бота]</a>"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Telebot')
async def process_callback_telebot(callback_query: types.CallbackQuery):
  article_text = "✨ <b>Статья:</b> <a href'https://telegra.ph/Telebot-razrabotka-bota-10-30'>[Telebot-о том как написать простого телеграм бота]</a>"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
