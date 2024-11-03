from aiogram import Bot, types

async def send_welcome(bot: Bot, chat_id: int, CHANNEL_USERNAME: str):
  try:
    chat_member = await bot.get_chat_member(CHANNEL_USERNAME, chat_id)
    if chat_member.status not in ['member', 'administrator', 'creator']:
      keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text="Подписаться", url=f"https://t.me/{CHANNEL_USERNAME}"))
      await bot.send_message(
        chat_id,
        "✨ Приветствую тебя в этом боте!\n\nС помощью него ты сможешь написать самого простого телеграм бота или модуль для какого-либо юзербота, не отрицаю что скоро в боте будет ещё много новых функций, но перед тем как ты познакомишься с материалами подпишись на мой канальчик по кнопке ниже ♡",
        parse_mode='HTML',
        reply_markup=keyboard
      )
    else:
      await bot.send_message(
        chat_id,
        "✨ Приветствую тебя в этом боте!\n\nС помощью него ты сможешь написать самого простого телеграм бота или модуль для какого-либо юзербота, не отрицаю что скоро в боте будет ещё много новых функций ♡",
        parse_mode='HTML'
      )
  except Exception as e:
    print(f'Ошибка при проверке подписки: {e}')

async def o_bote(bot: Bot, chat_id: int):
  await bot.send_message(
    chat_id,
    "🌟 Бот был написан на библиотеке Telethon и состоит из 5 файлов:\nmain.py - тут находится логика всех команд в обоих меню (боковом и нижнем)\nutils.py - в этом файле хранится большинство текстов и логика функций\nrequirements.txt - файл с зависимостями, необходимых для верной работы бота\nconfig.py - тут хранится токен бота\nREADME.md - здесь должна быть информация о боте, но я не заполняла, мне было лень\nИсходный код бота можете посмотреть здесь",
    parse_mode='HTML')

async def send_start_menu(bot: Bot, chat_id: int):
  keyboard = types.InlineKeyboardMarkup(row_width=2).add(
    types.InlineKeyboardButton("Hikka-Telethon", callback_data="Hikka-Telethon"),
    types.InlineKeyboardButton("RimTUB-Pyrogram", callback_data="RimTUB-Pyrogram"),
    types.InlineKeyboardButton("Pyrogram", callback_data="Pyrogram"),
    types.InlineKeyboardButton("Telethon", callback_data="Telethon"),
    types.InlineKeyboardButton("Telebot", callback_data="Telebot"),
  )
  await bot.send_message(chat_id, "💫 Выберите направление:", reply_markup=keyboard, parse_mode='HTML')

async def create_back_button(bot: Bot, chat_id: int):
  back_button = types.InlineKeyboardButton('Назад', callback_data="back")
  keyboard = types.InlineKeyboardMarkup(row_width=1).add(back_button)
  return keyboard
