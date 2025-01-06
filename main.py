from telethon import TelegramClient, events
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

app_api_id = os.getenv("APP_API_ID")
app_api_hash = os.getenv("APP_API_HASH")


client = TelegramClient('session_name', app_api_id, app_api_hash)


async def message_edit_task(event):
    message_text = event.raw_text.split(" ", 1)[1] # get the message text
    for i in range(1, len(message_text) + 1): # for each character in the message
        if message_text[i - 1] == " ":
            continue # skip spaces to avoid sending same message
        await event.edit(message_text[:i]) # edit the message with the first i characters
        await asyncio.sleep(0.5) 


@client.on(events.NewMessage(from_users='me'))
async def my_event_handler(event):
    if event.raw_text.startswith("/type") and len(event.raw_text.split(" ", 1)) > 1: # if the message starts with /type and has a message 
        await message_edit_task(event)
        

client.start()
client.run_until_disconnected()