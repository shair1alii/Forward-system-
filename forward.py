from telethon import TelegramClient, events, Button
import re

api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'

file_source = -1002545108359
file_forward_to = -1002739446626

otp_source = -1002781143657
otp_forward_to = -1003099447280

your_group_link = "https://t.me/NumberOtpGroup2"
your_channel_link = "https://t.me/NumberByMahid"

client = TelegramClient('user_forward_session', api_id, api_hash)

# 🔥 OTP extractor (strong version)
def extract_otp(text):
    if not text:
        return "0000"
    match = re.findall(r'\b\d{4,8}\b', text)
    return match[0] if match else "0000"

# ================= FILE FORWARD =================
@client.on(events.NewMessage(chats=file_source))
async def forward_file(event):
    if event.file:
        caption = event.raw_text or ""

        # clean text
        caption = re.sub(r'(@\w+|https?://\S+|t\.me/\S+)', '', caption)
        caption = caption.replace("@Rifat103300", "@MUNNABHAI_BD").strip()

        await client.send_file(
            file_forward_to,
            file=event.media,
            caption=caption,
            buttons=[
                Button.url("🔐 OTP Group Join Here", your_group_link)
            ]
        )

# ================= OTP SYSTEM =================
@client.on(events.NewMessage(chats=otp_source))
async def forward_otp(event):
    text = event.raw_text or ""

    text = text.replace("@Rifat103300", "@MUNNABHAI_BD")

    otp = extract_otp(text)

    # 🔥 IMPORTANT: custom rebuild buttons
    await client.send_message(
        otp_forward_to,
        f"{text}\n\n🔐 OTP: {otp}",
        buttons=[
            [Button.inline(f"📋 OTP: {otp}", data=f"otp_{otp}")],
            [
                Button.url("🔵 NUMBER GROUP", your_group_link),
                Button.url("📢 CHANNEL", your_channel_link)
            ]
        ]
    )

print("🚀 FULL SYSTEM RUNNING (FIXED OTP + BUTTONS)")
client.start()
client.run_until_disconnected()
