from telethon import TelegramClient, events
import requests
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

source_channel = os.getenv("SOURCE_CHANNEL")
webhook_url = os.getenv("WEBHOOK_URL")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):

    try:
        payload = {
            "text": event.raw_text,
            "date": str(event.date),
            "sender": str(event.sender_id)
        }

        requests.post(webhook_url, json=payload)

        print("Sent to n8n")

    except Exception as e:
        print("Error:", e)

print("Bot running...")

client.start()
client.run_until_disconnected()
