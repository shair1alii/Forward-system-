from telethon import TelegramClient, events, Button
import re

# ==== TELEGRAM API ====
api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'

# ==== CHANNEL / GROUP SETUP ====
file_source = -1002545108359         # File Channel
file_forward_to = -1002739446626     # Your Channel
otp_source = -1002717770463          # OTP Group
otp_forward_to = -1003099447280      # Your OTP Group

# ==== CUSTOM LINKS ====
your_group_link = "https://t.me/NumberOtpGroup2"
your_channel_link = "https://t.me/NumberByMahid"

client = TelegramClient('user_forward_session', api_id, api_hash)

# ✅ 1. FILE FORWARDING (with caption cleaned)
@client.on(events.NewMessage(chats=file_source))
async def forward_file(event):
    if event.file:
        caption = event.raw_text or ""
        # Remove unwanted links/usernames and "OTP : JOIN HERE"
        lines = caption.splitlines()
        cleaned_lines = [
            re.sub(r'(@\w+|https?://t\.me/\S+|t\.me/\S+|telegram\.me/\S+)', '', line)
            for line in lines
            if "OTP : JOIN HERE" not in line
        ]
        cleaned_caption = "\n".join(cleaned_lines).strip()
        # Replace old username with new one
        cleaned_caption = cleaned_caption.replace("@Rifat103300", "@MUNNABHAI_BD")
        await client.send_file(
            file_forward_to,
            file=event.media,
            caption=cleaned_caption,
            buttons=[Button.url("🔐 OTP Group Join Here", your_group_link)]
        )

# ✅ 2. OTP FORWARDING (only if contains 4-8 digit code)
@client.on(events.NewMessage(chats=otp_source))
async def forward_otp(event):
    text = event.raw_text
    # Replace old username with new one
    text = text.replace("@Rifat103300", "@MUNNABHAI_BD")
    if re.search(r'\b(\d{4,8})\b', text):
        await client.send_message(
            otp_forward_to,
            message=text,
            buttons=[Button.url("📢 Main Channel", your_channel_link)]
        )

print("✅ Forwarding system is running...")
client.start()
client.run_until_disconnected()
