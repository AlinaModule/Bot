from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import TOKEN, CHANNEL_USERNAME
from utils import send_welcome, o_bote, create_back_button

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Form(StatesGroup):
 name = State()
 age = State()

async def check_subscription(bot: Bot, chat_id: int, CHANNEL_USERNAME: str):
 try:
  chat_member = await bot.get_chat_member(CHANNEL_USERNAME, chat_id)
  if chat_member.status not in ['member', 'administrator', 'creator']:
   return False
  else:
   return True
 except Exception as e:
  print(f'Ошибка при проверке подписки: {e}')
  return False

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
 await send_welcome(bot, message.chat.id, CHANNEL_USERNAME)
 await send_main_menu(bot, message.chat.id)

@dp.message_handler(commands=['botinfo'])
async def cmd_botinfo(message: types.Message):
 if await check_subscription(bot, message.chat.id, CHANNEL_USERNAME):
  await o_bote(bot, message.chat.id)
 else:
  await send_welcome(bot, message.chat.id, CHANNEL_USERNAME)

@dp.message_handler(regexp=r"^\.(.*)")
async def handle_alias(message: types.Message):
 command = message.text[1:]
 if command == "старт":
  await cmd_start(message)
 elif command == "ботинфо":
  await cmd_botinfo(message)
 else:
  await message.reply("Неизвестная команда.")

@dp.callback_query_handler(text_contains="back")
async def back_callback(call: CallbackQuery, state: FSMContext):
  if call.data == "back_from_tg_bots":
   await send_main_menu(call.bot, call.message.chat.id)
  if call.data == "back_from_us":
   await send_main_menu(call.bot, call.message.chat.id)
  if call.data == 'back_from_tl":
   await send_main_menu(call.bot, call.message.chat.id)
  else:
    await call.message.edit_text("Ошибка: Неизвестное состояние")
    await call.answer()
   
@dp.callback_query_handler(lambda c: c.data == 'back')
async def process_callback_back(callback_query: types.CallbackQuery):
 await callback_query.message.edit_text("💫 Выберите направление:", reply_markup=create_main_menu(bot, callback_query.message.chat.id), parse_mode='HTML')
 await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'userbots')
async def process_callback_userbots(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  keyboard = types.InlineKeyboardMarkup(row_width=2).add(
   types.InlineKeyboardButton("Hikka-Telethon", callback_data="Hikka-Telethon"),
   types.InlineKeyboardButton("RimTUB-Pyrogram", callback_data="RimTUB-Pyrogram"),
   types.InlineKeyboardButton("Свой юзербот", callback_data="Свой_userbot"),
   types.InlineKeyboardButton("В меню", callback_data="back_from_us") 
  )
  await callback_query.message.edit_text("Выберите юзербота/библиотеку:", reply_markup=keyboard, parse_mode='HTML')
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'tg_bots')
async def process_callback_tg_bots(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  keyboard = types.InlineKeyboardMarkup(row_width=2).add(
   types.InlineKeyboardButton("Telethon", callback_data="Telethon"),
   types.InlineKeyboardButton("Pyrogram", callback_data="Pyrogram"),
   types.InlineKeyboardButton("Telebot", callback_data="Telebot"),
   types.InlineKeyboardButton("Aiogram", callback_data="Aiogram"),
   types.InlineKeyboardButton("Назад", callback_data="back_from_tg_bots") 
  )
  await callback_query.message.edit_text("Выберите библиотеку для написания бота:", reply_markup=keyboard, parse_mode='HTML')
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Hikka-Telethon')
async def process_callback_hikka(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  keyboard = types.InlineKeyboardMarkup("В меню", callback_data="back_from_tl") 
  )
  article_text = "🎆 Статья: [Telethon-про модули для Hikka]"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=keyboard)
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'RimTUB-Pyrogram')
async def process_callback_rimtub(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  article_text = "💉 <b>Статья:</b> <a href='https://telegra.ph/Pyrogram-pro-moduli-dlya-RimTUB-10-30'>[RimTUB-про то как написать для него модуль]</a>"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Свой_userbot')
async def process_callback_svoy_userbot(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  keyboard = types.InlineKeyboardMarkup(row_width=2).add(
   types.InlineKeyboardButton("Pyrogram", callback_data="Pyrogram_userbot"),
   types.InlineKeyboardButton("Telethon", callback_data="Telethon_userbot"),
  )
  await callback_query.message.edit_text("Выберите библиотеку для написания своего юзербота:", reply_markup=keyboard, parse_mode='HTML')
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Pyrogram')
async def process_callback_pyrogram(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  article_text = "📀 <b>Статья:</b> <a href='https://telegra.ph/Pyrogram-razrabotka-bota-10-30'>[Pyrogram-про то как написать простого телеграм бота]</a>"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Telethon')
async def process_callback_telethon(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  article_text = "⚙️ <b>Статья:</b> <a href='https://telegra.ph/Telethon-kak-napisat-svoego-telegram-bota-10-30'>[Telethon-про то как написать тг-бота]</a>"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Telebot')
async def process_callback_telebot(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  article_text = "⚙️ <b>Статья:</b> <a href='https://telegra.ph/Telebot-kak-napisat-svoego-telegram-bota-10-30'>[Telebot-про то как написать тг-бота]</a>"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Aiogram')
async def process_callback_aiogram(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  keyboard = types.InlineKeyboardMarkup(row_width=2).add(
    types.InlineKeyboardButton("aio2", callback_data="aio2"),
    types.InlineKeyboardButton("aio3", callback_data="aio3"),
  )
  await callback_query.message.edit_text("Выберите версию aio:", reply_markup=keyboard, parse_mode='HTML')
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'aio2')
async def process_callback_aio2(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  article_text = "Статья [пустая 3]"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'aio3')
async def process_callback_aio3(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  article_text = "Статья [пустая 4]"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Pyrogram_userbot')
async def process_callback_pyrogram_userbot(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  article_text = "Статья [пустая 1]"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

@dp.callback_query_handler(lambda c: c.data == 'Telethon_userbot')
async def process_callback_telethon_userbot(callback_query: types.CallbackQuery):
 if await check_subscription(bot, callback_query.message.chat.id, CHANNEL_USERNAME):
  article_text = "Статья [пустая 2]"
  await callback_query.message.edit_text(article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()
 else:
  await callback_query.message.edit_text("Сначала подпишись на канал!", reply_markup=create_back_button(bot, callback_query.message.chat.id))
  await callback_query.answer()

async def send_main_menu(bot: Bot, chat_id: int):
 keyboard = types.InlineKeyboardMarkup(row_width=2).add(
  types.InlineKeyboardButton("Юзерботы", callback_data="userbots"),
  types.InlineKeyboardButton("ТГ-боты", callback_data="tg_bots"),
 )
 await bot.send_message(chat_id, "💫 Выберите направление:", reply_markup=keyboard, parse_mode='HTML')

async def send_start_menu(bot: Bot, chat_id: int):
 await bot.send_message(chat_id, "💫 Выберите направление:", parse_mode='HTML')

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
