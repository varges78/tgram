from telethon import TelegramClient, events

api_id = '19156942'
api_hash = '341ed94ec15ab328b837b4ce4c3ced55'

client = TelegramClient('anon', api_id, api_hash)
client.start()

# Pocket Option Official Signal Bot
@client.on(events.NewMessage(1385109737))
async def main(event):
            await client.send_message(-1001166633924, event.message) # WINBINARY
            await client.send_message(-1001547454993, event.message) # ПРОФИТНЫЕ СИГНАЛЫ

# Live прогнозы и ставки на спорт
@client.on(events.NewMessage(-1001342598437))
async def main(event):
     await client.send_message(-1001094033192, event.message) # VARGES CLUB
     await client.send_message(-1001250994275, event.message) # BEARETOR BETS

client.run_until_disconnected()
