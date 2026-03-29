from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon import Button
import re

#  ===== Telegram API =====
api_id = 21367965
api_hash = "198b8590c4c2656e8bc4e2b721e71416"

# ===== session string =====
session_str = "1BJWap1sBuwNGiy9EYUCKi-XtpadrG5rEd0Ti8yUwMVS-_foR2Tki9wCvJzH9XRxZ3NYuE59tli5THrLQ78coscp6PNSmKRW2WAgSBrIstZSSvSnNU4dAHRTif3FwT7CUTCgZaTbBUujoUSKivwlC-Xv56Yd8q8KsEeGwu6GWqcbLuKhvuQrvR7qwI7hvY4Te0l-jblYEiTYUiQYy4lbwsnhvZI2Brf-OQVnttLjiJyPEDaAsT4kFWPint5Mf5PFtSTQGJyeQY0dLpBuemIwpXDHIFIncqr1dHwtreX6I1IJjbIHpN9V89hXixA6Q8cMtmr9cyvHyOHrXePBKdgVD_qAD2NT1yBI="

# ===== group IDs =====
source_group = -1002781143657
target_group = -1003099447280

# Custom name replacement
custom_name = "AliSheir"

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    msg_text = event.message.text

    # ===== Extract number (like 584 PAK CYBER 568) =====
    # Simple regex, adjust if pattern different
    number_match = re.search(r'\d{3}\s\w+\s\w+\s\d{3}', msg_text)
    if number_match:
        number_text = number_match.group()
        # Replace first part with custom name + XX
        number_text = re.sub(r'^\d{3}', f"{custom_name} XX", number_text)
    else:
        number_text = msg_text  # fallback

    # ===== Extract OTP (assume numeric code 4-6 digits in message) =====
    otp_match = re.search(r'\b\d{4,6}\b', msg_text)
    otp_text = otp_match.group() if otp_match else "OTP"

    # ===== Send to target group with buttons =====
    await client.send_message(
        target_group,
        number_text,
        buttons=[
            [Button.inline(f"OTP: {otp_text}", data=f"otp_{otp_text}")],
            [Button.url("My Channel", url="https://t.me/YOUR_CHANNEL")]
        ]
    )

client.start()
client.run_until_disconnected()