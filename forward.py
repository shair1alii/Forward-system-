from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import re
import asyncio

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'
session_str = "1BJWap1sBu2ZbByWOF3_atudHlU6habv8jwd8Hk-c92BEkBBqEDehvAICIiAMKgKPsMlCRAoVm8tP2QiLr8oA1Zo0F-Q_ypTND2qzga59Bh5oApKoelWJoewqNEnKsSKcumpAcOR30YctPG1IJQe3KulNROo24zNa7hZbXBBumzsJzMr6ZSR0BHkU_1dc8o6ZFx-y6jdOCuC8sncNOCnrCELm6jhXftZkuYNg6YH8ts03r9qtGbPexyY-iqBgD5t8O3IWVOtz4j5oxhQCIBPaxjxanwCWwqWnW58gdzd_UuDFwNbOOgjEyNjLGXFtfB7fOM3IvKEDTnf7Cj9wmBjNMoChtrZ6mR8="

otp_source = -1002781143657
otp_forward_to = -1003099447280

client = TelegramClient(StringSession(session_str), api_id, api_hash)

# 🔥 extract OTP from button text like 792-663
def extract_otp_from_button(msg):
    if not msg.buttons:
        return None

    for row in msg.buttons:
        for btn in row:
            if hasattr(btn, "text"):
                txt = btn.text.replace("-", "")
                if txt.isdigit() and 4 <= len(txt) <= 8:
                    return btn.text  # return original format

    return None

@client.on(events.NewMessage(chats=otp_source))
async def handler(event):
    msg = event.message

    otp_text = extract_otp_from_button(msg)

    buttons = None
    if otp_text:
        buttons = [[Button.inline(f"📋 {otp_text}", data=f"otp_{otp_text}")]]

    await client.send_message(
        otp_forward_to,
        msg.message or "",
        buttons=buttons
    )

async def main():
    print("🚀 Hybrid bot running...")

    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Session invalid")
        return

    print("✅ Connected")

    await client.run_until_disconnected()

asyncio.run(main())
