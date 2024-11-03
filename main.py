from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re
from config import TOKEN, CHANNEL_USERNAME
from utils import send_welcome, send_start_menu, create_back_button, o_bote

app = Client("my_bot", bot_token=TOKEN, api_id=284726637, api_hash="dc6ef4cd93a26131aa5881052149049") 

PREFIX = "/"

@app.on_message(filters.command(f"{PREFIX}start", prefixes=["/", "!", ".", "*"],))
async def start_command(client, message):
    await send_welcome(client, message.chat.id, CHANNEL_USERNAME)
    await send_start_menu(client, message.chat.id)

@app.on_message(filters.command(f"{PREFIX}botinfo", prefixes=["/", "!", ".", "*"],))
async def o_bote_command(client, message):
    try:
        chat_member = await client.get_chat_member(CHANNEL_USERNAME, message.chat.id)
        if chat_member.status not in ['member', 'administrator', 'creator']:
            await send_welcome(client, message.chat.id, CHANNEL_USERNAME)
            return
    except Exception as e:
        print(f'error: {e}')
    await o_bote(client, message.chat.id)

@app.on_message(filters.text)
async def handle_alias(client, message):
    text = message.text.strip()
    
    if text.startswith("."):
        command = text[1:] 
    else:
        match = re.match(r"^/(.*)", text)
        if match:
            command = match.group(1)
        else:
            return  

    if command == "старт":
        await start_command(client, message)
    elif command == "ботинфо":
        await o_bote_command(client, message)
    else:
        return

@app.on_callback_query()
async def callback_query_handler(client, query):
    chat_id = query.message.chat.id
    data = query.data

    if data == "back":
        await send_start_menu(client, chat_id)
        await query.message.delete()
    elif data == "Hikka-Telethon":
        article_text = "🎆 <b>Статья:</b> <a href='https://telegra.ph/Telethon-pro-moduli-dlya-Hikka-10-30'>[Telethon-про модули для Hikka]</a>"
        await client.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        await query.message.delete()
    elif data == "RimTUB-Pyrogram":
        article_text = "💉 <b>Статья:</b> <a href='https://telegra.ph/Pyrogram-pro-moduli-dlya-RimTUB-10-30'>[RimTUB-про то как написать для него модуль]</a>"
        await client.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        await query.message.delete()
    elif data == "Pyrogram":
        article_text = "📀 <b>Статья:</b> <a href='https://telegra.ph/Pyrogram-razrabotka-bota-10-30'>[Pyrogram-про то как написать простого телеграм бота]</a>"
        await client.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        await query.message.delete()
    elif data == "Telethon":
        article_text = "⚙️ <b>Статья:</b> <a href='https://telegra.ph/Telethon-kak-napisat-svoego-telegram-bota-10-30'>[Telethon-про то как написать тг-бота]</a>"
        await client.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        await query.message.delete()
    elif data == "Telebot":
        article_text = "✨ <b>Статья:</b> <a href'https://telegra.ph/Telebot-razrabotka-bota-10-30'>[Telebot-о том как написать простого телеграм бота]</a>"
        await client.send_message(chat_id, article_text, disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_back_button())
        await query.message.delete()
 
app.run()
