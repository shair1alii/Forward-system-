from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import re

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'
session_str = "1BJWap1sBu2ZbByWOF3_atudHlU6habv8jwd8Hk-c92BEkBBqEDehvAICIiAMKgKPsMlCRAoVm8tP2QiLr8oA1Zo0F-Q_ypTND2qzga59Bh5oApKoelWJoewqNEnKsSKcumpAcOR30YctPG1IJQe3KulNROo24zNa7hZbXBBumzsJzMr6ZSR0BHkU_1dc8o6ZFx-y6jdOCuC8sncNOCnrCELm6jhXftZkuYNg6YH8ts03r9qtGbPexyY-iqBgD5t8O3IWVOtz4j5oxhQCIBPaxjxanwCWwqWnW58gdzd_UuDFwNbOOgjEyNjLGXFtfB7fOM3IvKEDTnf7Cj9wmBjNMoChtrZ6mR8="

otp_source = -1002781143657
otp_forward_to = -1003099447280

client = TelegramClient(StringSession(session_str), api_id, api_hash)


# 🔥 extract ONLY button OTP (priority)
def extract_button_otp(msg):
    if not msg.buttons:
        return None

    for row in msg.buttons:
        for btn in row:
            if hasattr(btn, "text"):
                t = btn.text.strip()

                # only numeric OTP (1-10 digits)
                if re.fullmatch(r"\d{1,10}", t):
                    return t

    return None


# 🔥 fallback: text se OTP
def extract_text_otp(text):
    m = re.findall(r"\b\d{4,10}\b", text or "")
    return m[0] if m else None


@client.on(events.NewMessage(chats=otp_source))
async def handler(event):
    msg = event.message

    # 1️⃣ button OTP first priority
    otp = extract_button_otp(msg)

    # 2️⃣ fallback text OTP
    if not otp:
        otp = extract_text_otp(msg.message)

    # 3️⃣ send clean format
    if otp:
        await client.send_message(
            otp_forward_to,
            f"OTP: {otp}",
            buttons=[
                [Button.inline(f"📋 Copy OTP ({otp})", data=f"copy_{otp}")]
            ]
        )
    else:
        # fallback raw message
        await client.send_message(
            otp_forward_to,
            msg.message or ""
        )


async def main():
    print("🚀 OTP BOT RUNNING...")
    await client.start()
    print("✅ Connected")
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
