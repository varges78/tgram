from telethon import TelegramClient, events

api_id = '19156942'
api_hash = '341ed94ec15ab328b837b4ce4c3ced55'

client = TelegramClient('anon', api_id, api_hash)
client.start()

# Pocket Option Official Signal Bot
@client.on(events.NewMessage(1385109737))
async def main(event):
    # @client.message_handler(content_types=['text'])
    # def send_text(message):
        # string = message.text.lower()
        # substring = 'символ'
        # if string.find(substring) > -1:
            await client.send_message(-1001548724631, event.message)

# ORLOW TRADING CLUB
@client.on(events.NewMessage(-1001226882428))
async def main(event):
     await client.send_message(-1001548724631, event.message)


# Live прогнозы и ставки на спорт
@client.on(events.NewMessage(-1001226882428))
async def main(event):
     await client.send_message(-1001342598437, event.message)


# ФАРМИМ БАБЛО
@client.on(events.NewMessage(-1001358758220))
async def main(event):
     await client.send_message(-1001548724631, event.message)

client.run_until_disconnected()