from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import re
import asyncio

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'
session_str = "1BJWap1sBuzwTc3_Y2x5zFDnADXX02ycXfMtkWnu0Du56qy-_-H0sKaJcOc5t8oYAUzXWDWalcSh-UlzkrjkQpc-oPVPP6TfS5zOn_Czdm958wWR5VUEEdTcTbTFeKgKLh-XVImSLAsQnm8TqniQkpAJCU13fC9Z48-AB-9_OodFQBQi5CZyVZPnO8TmllQDbJ1tfFnjX2Lx6asnVtjcqQRPJFxbcsexu4br_Uj-eRl0GIbh_Uj4j5MBPg69bggLMsY3ZlYzf8dLwTTl8OfOiG519VJ1lR33OZZc1LdE_VoVfXlf1T7Nzsu_DHK93Cwc4QyAQsinS9icFbK4wqXoFn5aMX1ZGmUs="

file_source = -1002545108359
file_forward_to = -1002739446626

otp_source = -1002781143657
otp_forward_to = -1003099447280

your_group_link = "https://t.me/NumberOtpGroup2"
your_channel_link = "https://t.me/NumberByMahid"

client = TelegramClient(StringSession(session_str), api_id, api_hash)

# 🔥 FIXED OTP EXTRACTOR (TEXT + BUTTON SUPPORT)
def extract_otp(event):
    text = event.raw_text or ""

    # 1st: normal text OTP
    match = re.findall(r'\b\d{4,8}\b', text)
    if match:
        return match[0]

    # 2nd: button OTP (IMPORTANT FIX)
    if event.message.buttons:
        for row in event.message.buttons:
            for btn in row:
                if hasattr(btn, "text"):
                    match2 = re.findall(r'\b\d{4,8}\b', btn.text)
                    if match2:
                        return match2[0]

    return "0000"

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
    otp = extract_otp(event)

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

    # ❌ FIX: client.start() removed (session already used)
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Session invalid!")
        return

    print("✅ Connected!")

    await client.run_until_disconnected()

asyncio.run(main())
