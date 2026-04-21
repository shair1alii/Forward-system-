from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession   # ✅ ADD THIS
import re

# ==== TELEGRAM API ====
api_id = 21367965
api_hash = '198b8590c4c2656e8bc4e2b721e71416'

# ==== STRING SESSION ====
string_session = "1BJWap1sBu4JZcr_KroJIYb9_1Arweuvxyw4QBwkZfJ3HqxfSWNBKGnVzA_6r887c83Qu88R2w7rUKsVZKOSOPkWKB7O4wd0uoIOEzMdk_4gB8FU0sTMV97fXgaP4S6dllJktUxkTSm5KrxZEmhKVSdKVltbB6G6MmdCWnX5lmGOGEFOTg7JhuZD3SzBm93RmO9tMJioIIoACnNPphRanRKmEMIe3rZpLvIXR0tFri41LaP4LvY4tF_OPuZ6KNsr-ziNPahjNA0_xefKpCKpaM4OzGcMQNSJjA7oYGIeLV93qcoNgsL8umzrSuJ97jBlCcIDT97NXyy52N_mjvvhaPbag_v4LYu8="   # ✅ ADD THIS

# ==== CHANNEL / GROUP SETUP ====
file_source = -1002545108359
file_forward_to = -1002739446626
otp_source = -1002717770463
otp_forward_to = -1003099447280

# ==== CUSTOM LINKS ====
your_group_link = "https://t.me/NumberOtpGroup2"
your_channel_link = "https://t.me/NumberByMahid"

# ❌ OLD:
# client = TelegramClient('user_forward_session', api_id, api_hash)

# ✅ NEW:
client = TelegramClient(StringSession(string_session), api_id, api_hash)

# ✅ 1. FILE FORWARDING
@client.on(events.NewMessage(chats=file_source))
async def forward_file(event):
    if event.file:
        caption = event.raw_text or ""
        lines = caption.splitlines()
        cleaned_lines = [
            re.sub(r'(@\w+|https?://t\.me/\S+|t\.me/\S+|telegram\.me/\S+)', '', line)
            for line in lines
            if "OTP : JOIN HERE" not in line
        ]
        cleaned_caption = "\n".join(cleaned_lines).strip()
        cleaned_caption = cleaned_caption.replace("@Rifat103300", "@MUNNABHAI_BD")

        await client.send_file(
            file_forward_to,
            file=event.media,
            caption=cleaned_caption,
            buttons=[Button.url("🔐 OTP Group Join Here", your_group_link)]
        )

# ✅ 2. OTP FORWARDING
@client.on(events.NewMessage(chats=otp_source))
async def forward_otp(event):
    text = event.raw_text or ""   # ✅ small fix
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
