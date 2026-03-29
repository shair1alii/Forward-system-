from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
import re

api_id = 21367965
api_hash = "198b8590c4c2656e8bc4e2b721e71416"
session_str = "1BJWap1sBu3AD76nUYOEND59Hc565P-xQutIxbBYgZnjEiF2IomMU2HR5V56ALCeAcDluAqVIQtjnjyEkYsJwjZ5fknDSXOtw5T6HvndDYkIjvtZROYtCujPku7xtpRr8cvQG04IkwbaftrE-2h-iHxNsS3YYCP8Mf6w7WiAMOplQPve89yEM9mNcQ83JRK4e_FpIVXm_ySZGTpjrGdJifJuxMz_aq3dYlHIvGiJDc7_o-SEBUICRoOOU1Qyl45Wk6oaHk1QYKpA9fajuLcjPRDZ-zi9niyC7sxwHmcuM1rgq7FA9WDYhqr29n6BQq-EkV1eHCqn9cAGsXzLR6t-zm9m2oFsc92o="

source_group = -1002781143657
target_group = -1003099447280

client = TelegramClient(StringSession(session_str), api_id, api_hash)

def format_box(country, number):
    return f"""╭────────────────────╮
│ 📱 {country}  #{number}
╰────────────────────╯"""

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    msg_text = event.message.text or ""

    # Country detect
    if "#PK" in msg_text:
        flag = "🇵🇰"
        country = "#PK"
    elif "#VE" in msg_text:
        flag = "🇻🇪"
        country = "#VE"
    else:
        flag = "🌍"
        country = "#OT"

    # Number extract
    number_match = re.search(r'\d{4,}', msg_text)
    number = number_match.group() if number_match else "XXXXXXXX"

    if len(number) > 6:
        number = number[:4] + "XX" + number[-3:]

    # OTP extract
    otp_match = re.search(r'\b\d{4,6}\b', msg_text)
    otp = otp_match.group() if otp_match else "000000"

    text = format_box(flag, f"{country} {number}")

    await client.send_message(
        target_group,
        text,
        buttons=[
            [Button.inline(f"📋 {otp}", data=f"copy_{otp}")],
            [
                Button.url("🔵 NUMBERS", url="https://t.me/Ali_OldHacker"),
                Button.url("🔴 BACKUP", url="https://t.me/Ali_OldHacker")
            ]
        ]
    )

client.start()
client.run_until_disconnected()
