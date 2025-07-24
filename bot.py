import asyncio
from telegram import Bot

TOKEN = "8350943832:AAFyO8AB7ZB6Zv2ytn2PLCTnBjO3U6gfdJE"

async def main():
    bot = Bot(token=TOKEN)
    me = await bot.get_me()
    print(me)

asyncio.run(main())
