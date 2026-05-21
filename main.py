```python
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

    message_text = event.raw_text if event.raw_text else ""

    data = {
        "text": message_text
    }

    try:
        requests.post(webhook_url, json=data)
        print("Message sent to n8n")
    except Exception as e:
        print("Error:", e)

print("Bot Started...")

client.start()
client.run_until_disconnected()
```
