import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import TelegramError

# Load environment variables
load_dotenv()

# Get token from environment variable
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    if not TOKEN:
        print("Error: BOT_TOKEN not found in environment variables")
        return
    
    try:
        bot = Bot(token=TOKEN)
        me = await bot.get_me()
        print(f"Bot connected successfully!")
        print(f"Bot name: {me.first_name}")
        print(f"Bot username: @{me.username}")
        print(f"Bot ID: {me.id}")
    except TelegramError as e:
        print(f"Telegram API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
