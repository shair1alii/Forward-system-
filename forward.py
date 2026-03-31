from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import asyncio

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'
session_str = "1BJWap1sBu2ZbByWOF3_atudHlU6habv8jwd8Hk-c92BEkBBqEDehvAICIiAMKgKPsMlCRAoVm8tP2QiLr8oA1Zo0F-Q_ypTND2qzga59Bh5oApKoelWJoewqNEnKsSKcumpAcOR30YctPG1IJQe3KulNROo24zNa7hZbXBBumzsJzMr6ZSR0BHkU_1dc8o6ZFx-y6jdOCuC8sncNOCnrCELm6jhXftZkuYNg6YH8ts03r9qtGbPexyY-iqBgD5t8O3IWVOtz4j5oxhQCIBPaxjxanwCWwqWnW58gdzd_UuDFwNbOOgjEyNjLGXFtfB7fOM3IvKEDTnf7Cj9wmBjNMoChtrZ6mR8="

otp_source = -1002781143657
otp_forward_to = -1003099447280

client = TelegramClient(StringSession(session_str), api_id, api_hash)

# 🔥 ONLY OTP BUTTON FILTER
def get_otp_button(msg):
    if not msg.buttons:
        return None

    for row in msg.buttons:
        for btn in row:
            # 👉 green OTP button usually digits format
            if hasattr(btn, "text"):
                txt = btn.text.replace("-", "").replace(" ", "")
                if txt.isdigit() and 4 <= len(txt) <= 8:
                    return btn

    return None

@client.on(events.NewMessage(chats=otp_source))
async def handler(event):
    msg = event.message

    # 🔥 find only OTP button
    otp_btn = get_otp_button(msg)

    buttons = None
    if otp_btn:
        buttons = [[otp_btn]]  # only 1 button

    await client.send_message(
        otp_forward_to,
        msg.message or "",
        buttons=buttons
    )

async def main():
    print("🚀 Running FINAL OTP SYSTEM...")

    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Session invalid")
        return

    print("✅ Connected")

    await client.run_until_disconnected()

asyncio.run(main())
