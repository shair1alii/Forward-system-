from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import re

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'
session_str = "1BJWap1sBu4JZcr_KroJIYb9_1Arweuvxyw4QBwkZfJ3HqxfSWNBKGnVzA_6r887c83Qu88R2w7rUKsVZKOSOPkWKB7O4wd0uoIOEzMdk_4gB8FU0sTMV97fXgaP4S6dllJktUxkTSm5KrxZEmhKVSdKVltbB6G6MmdCWnX5lmGOGEFOTg7JhuZD3SzBm93RmO9tMJioIIoACnNPphRanRKmEMIe3rZpLvIXR0tFri41LaP4LvY4tF_OPuZ6KNsr-ziNPahjNA0_xefKpCKpaM4OzGcMQNSJjA7oYGIeLV93qcoNgsL8umzrSuJ97jBlCcIDT97NXyy52N_mjvvhaPbag_v4LYu8="

otp_source = -1002717770463
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
