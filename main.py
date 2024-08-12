import asyncio
import json
from datetime import datetime
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message, Chat

# load configurations
config = json.load(open("config.json", "r", encoding="utf-8"))
API_ID = int(config["api_id"])
API_HASH = config["api_hash"]
# channel id
CHANNEL = config["channel_id"]

app = Client(name="zone_file_remover", api_id=API_ID, api_hash=API_HASH)


@app.on_message(filters.channel & filters.command(commands=["delete"], prefixes=["!", "/"]))
async def forward(client: Client, message: Message):
    chat: Chat = message.chat
    await client.delete_messages(chat_id=chat.id, message_ids=message.id)
    messages = client.get_chat_history(chat_id=chat.id)
    total = 0
    async for message in messages:
        await client.delete_messages(chat_id=chat.id, message_ids=message.id)
        print(
            f"Message {message.text} has been deleted - {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}")
        total += 1
        await asyncio.sleep(.5)
    print(f"Total messages deleted : {total}")


print("[Started] Zone file remover bot - waiting for tasks :)")
app.run()
