from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import re
import asyncio

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'
session_str = "YOUR_SESSION_HERE"

file_source = -1002545108359
file_forward_to = -1002739446626

otp_source = -1002781143657
otp_forward_to = -1003099447280

your_group_link = "https://t.me/NumberOtpGroup2"
your_channel_link = "https://t.me/NumberByMahid"

client = TelegramClient(StringSession(session_str), api_id, api_hash)

def extract_otp(text):
    match = re.findall(r'\b\d{4,8}\b', text or "")
    return match[0] if match else "0000"

@client.on(events.NewMessage(chats=file_source))
async def forward_file(event):
    if event.file:
        await client.send_file(
            file_forward_to,
            event.media,
            caption=event.raw_text or ""
        )

@client.on(events.NewMessage(chats=otp_source))
async def forward_otp(event):
    text = event.raw_text or ""
    otp = extract_otp(text)

    await client.send_message(
        otp_forward_to,
        f"{text}\n\n🔐 OTP: {otp}",
        buttons=[
            [Button.inline(f"📋 OTP: {otp}", data=f"otp_{otp}")],
            [
                Button.url("🔵 GROUP", your_group_link),
                Button.url("📢 CHANNEL", your_channel_link)
            ]
        ]
    )

async def main():
    print("🚀 Bot starting...")

    await client.start()
    print("✅ Connected!")

    await client.run_until_disconnected()

# 🔥 IMPORTANT: proper async run
asyncio.run(main())
