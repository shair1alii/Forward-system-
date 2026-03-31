from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import re
import asyncio

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'
session_str = "1BJWap1sBu2ZbByWOF3_atudHlU6habv8jwd8Hk-c92BEkBBqEDehvAICIiAMKgKPsMlCRAoVm8tP2QiLr8oA1Zo0F-Q_ypTND2qzga59Bh5oApKoelWJoewqNEnKsSKcumpAcOR30YctPG1IJQe3KulNROo24zNa7hZbXBBumzsJzMr6ZSR0BHkU_1dc8o6ZFx-y6jdOCuC8sncNOCnrCELm6jhXftZkuYNg6YH8ts03r9qtGbPexyY-iqBgD5t8O3IWVOtz4j5oxhQCIBPaxjxanwCWwqWnW58gdzd_UuDFwNbOOgjEyNjLGXFtfB7fOM3IvKEDTnf7Cj9wmBjNMoChtrZ6mR8="

file_source = -1002545108359
file_forward_to = -1002739446626

otp_source = -1002781143657
otp_forward_to = -1003099447280

your_group_link = "https://t.me/NumberOtpGroup2"
your_channel_link = "https://t.me/NumberByMahid"

client = TelegramClient(StringSession(session_str), api_id, api_hash)

# 🔥 ULTRA FIXED OTP EXTRACTOR (TEXT + BUTTON + CALLBACK DATA)
def extract_otp(event):
    text = event.raw_text or ""

    # 1️⃣ normal text OTP
    match = re.findall(r'\b\d{4,8}\b', text)
    if match:
        return match[0]

    # 2️⃣ button + callback OTP (REAL FIX)
    if event.message.buttons:
        for row in event.message.buttons:
            for btn in row:

                # TEXT button
                if hasattr(btn, "text") and btn.text:
                    m = re.findall(r'\b\d{4,8}\b', btn.text)
                    if m:
                        return m[0]

                # 🔥 CALLBACK DATA (IMPORTANT FIX FOR YOUR CASE)
                if hasattr(btn, "data") and btn.data:
                    try:
                        data_str = btn.data.decode("utf-8")
                    except:
                        data_str = str(btn.data)

                    m2 = re.findall(r'\b\d{4,8}\b', data_str)
                    if m2:
                        return m2[0]

    return "0000"

# 📦 FILE FORWARD
@client.on(events.NewMessage(chats=file_source))
async def forward_file(event):
    if event.file:
        await client.send_file(
            file_forward_to,
            event.media,
            caption=event.raw_text or ""
        )

# 🔐 OTP FORWARD (FIXED)
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

# 🚀 MAIN RUNNER (FIXED SAFE VERSION)
async def main():
    print("🚀 Bot starting...")

    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Session invalid!")
        return

    print("✅ Connected!")

    await client.run_until_disconnected()

asyncio.run(main())
