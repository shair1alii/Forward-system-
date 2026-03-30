from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession

api_id = 21367965
api_hash = "198b8590c4c2656e8bc4e2b721e71416"
session_str = "1BJWap1sBu3AD76nUYOEND59Hc565P-xQutIxbBYgZnjEiF2IomMU2HR5V56ALCeAcDluAqVIQtjnjyEkYsJwjZ5fknDSXOtw5T6HvndDYkIjvtZROYtCujPku7xtpRr8cvQG04IkwbaftrE-2h-iHxNsS3YYCP8Mf6w7WiAMOplQPve89yEM9mNcQ83JRK4e_FpIVXm_ySZGTpjrGdJifJuxMz_aq3dYlHIvGiJDc7_o-SEBUICRoOOU1Qyl45Wk6oaHk1QYKpA9fajuLcjPRDZ-zi9niyC7sxwHmcuM1rgq7FA9WDYhqr29n6BQq-EkV1eHCqn9cAGsXzLR6t-zm9m2oFsc92o="

source_group = -1002781143657
target_group = -1003099447280

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    try:
        msg = event.message

        # ✅ اگر text ہو
        if msg.text:
            await client.send_message(target_group, msg.text)

        # ✅ اگر photo/video/file ہو
        elif msg.media:
            await client.send_file(
                target_group,
                msg.media,
                caption=msg.text or ""
            )

    except Exception as e:
        print("Error:", e)

print("✅ Userbot is running...")
client.start()
client.run_until_disconnected()
