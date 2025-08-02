# Telegram Bot Project

A simple Telegram bot that connects to the Telegram API and displays bot information.

## Setup

1. **Install Python dependencies:**
   ```bash
   sudo apt install python3.13-venv
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   Create a `.env` file in the project root with your bot token:
   ```
   BOT_TOKEN=your_bot_token_here
   ```

3. **Run the bot:**
   ```bash
   source venv/bin/activate
   python bot.py
   ```

## Features

- Connects to Telegram Bot API
- Displays bot information (name, username, ID)
- Error handling for API issues
- Secure token management using environment variables

## Requirements

- Python 3.13+
- python-telegram-bot>=20.0
- pymongo
- python-dotenv