from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import re

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'
session_str = "1BJWap1sBu2ZbByWOF3_atudHlU6habv8jwd8Hk-c92BEkBBqEDehvAICIiAMKgKPsMlCRAoVm8tP2QiLr8oA1Zo0F-Q_ypTND2qzga59Bh5oApKoelWJoewqNEnKsSKcumpAcOR30YctPG1IJQe3KulNROo24zNa7hZbXBBumzsJzMr6ZSR0BHkU_1dc8o6ZFx-y6jdOCuC8sncNOCnrCELm6jhXftZkuYNg6YH8ts03r9qtGbPexyY-iqBgD5t8O3IWVOtz4j5oxhQCIBPaxjxanwCWwqWnW58gdzd_UuDFwNbOOgjEyNjLGXFtfB7fOM3IvKEDTnf7Cj9wmBjNMoChtrZ6mR8="

otp_source = -1002781143657
otp_forward_to = -1003099447280

client = TelegramClient(StringSession(session_str), api_id, api_hash)

# 🔥 Extract OTP from text + buttons
def extract_otp(msg):
    text = msg.message or ""

    # 1️⃣ text se digits
    numbers = re.findall(r'\b\d{1,8}\b', text)

    otp_from_text = numbers[0] if numbers else ""

    # 2️⃣ buttons se numbers/words collect
    button_parts = []

    if msg.buttons:
        for row in msg.buttons:
            for btn in row:
                if hasattr(btn, "text"):
                    clean = btn.text.strip()

                    # only take digits or small words (like 1-10 or code parts)
                    if re.fullmatch(r'[0-9]+', clean):
                        button_parts.append(clean)
                    elif len(clean) <= 10:
                        button_parts.append(clean)

    # 3️⃣ combine all parts
    final_otp = otp_from_text + "".join(button_parts)

    # optional: keep only digits (clean OTP)
    final_otp_digits = re.sub(r'\D', '', final_otp)

    return final_otp_digits


@client.on(events.NewMessage(chats=otp_source))
async def handler(event):
    msg = event.message

    otp = extract_otp(msg)

    if otp:
        await client.send_message(
            otp_forward_to,
            msg.message or "",
            buttons=[
                [Button.inline(f"📋 OTP: {otp}", data=f"otp_{otp}")]
            ]
        )
    else:
        await client.send_message(
            otp_forward_to,
            msg.message or ""
        )


async def main():
    print("🚀 BOT RUNNING...")
    await client.start()
    print("✅ Connected")
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
