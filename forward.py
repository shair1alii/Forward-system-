from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 21367965
api_hash = "198b8590c4c2656e8bc4e2b721e71416"
session_str = "1BJWap1sBuzwTc3_Y2x5zFDnADXX02ycXfMtkWnu0Du56qy-_-H0sKaJcOc5t8oYAUzXWDWalcSh-UlzkrjkQpc-oPVPP6TfS5zOn_Czdm958wWR5VUEEdTcTbTFeKgKLh-XVImSLAsQnm8TqniQkpAJCU13fC9Z48-AB-9_OodFQBQi5CZyVZPnO8TmllQDbJ1tfFnjX2Lx6asnVtjcqQRPJFxbcsexu4br_Uj-eRl0GIbh_Uj4j5MBPg69bggLMsY3ZlYzf8dLwTTl8OfOiG519VJ1lR33OZZc1LdE_VoVfXlf1T7Nzsu_DHK93Cwc4QyAQsinS9icFbK4wqXoFn5aMX1ZGmUs="

source_group = -1002781143657
target_group = -1003099447280

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    try:
        msg = event.message

        await client.send_message(
            target_group,
            msg.text or "",
            buttons=msg.reply_markup  # 🔥 REAL FIX
        )

    except Exception as e:
        print("Error:", e)

print("✅ Running fixed bot (buttons enabled)...")
client.start()
client.run_until_disconnected()
