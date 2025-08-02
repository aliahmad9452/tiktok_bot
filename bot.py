import asyncio
import logging
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "8350943832:AAFyO8AB7ZB6Zv2ytn2PLCTnBjO3U6gfdJE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with the main menu when the command /start is issued."""
    keyboard = [
        [
            InlineKeyboardButton("📊 Statistics", callback_data='statistics'),
            InlineKeyboardButton("⚙️ Settings", callback_data='settings')
        ],
        [
            InlineKeyboardButton("ℹ️ Help", callback_data='help'),
            InlineKeyboardButton("📞 Contact", callback_data='contact')
        ],
        [
            InlineKeyboardButton("🎮 Games", callback_data='games'),
            InlineKeyboardButton("🔧 Tools", callback_data='tools')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🤖 Welcome to your Telegram Bot!\n\n"
        "Please select an option from the menu below:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()  # Answer the callback query to remove the loading state
    
    if query.data == 'statistics':
        await query.edit_message_text(
            "📊 **Statistics**\n\n"
            "• Total users: 0\n"
            "• Messages processed: 0\n"
            "• Bot uptime: 0 minutes\n\n"
            "This is a sample statistics page.",
            parse_mode='Markdown'
        )
    elif query.data == 'settings':
        await query.edit_message_text(
            "⚙️ **Settings**\n\n"
            "• Language: English\n"
            "• Notifications: Enabled\n"
            "• Auto-reply: Disabled\n\n"
            "Settings configuration will be available here.",
            parse_mode='Markdown'
        )
    elif query.data == 'help':
        await query.edit_message_text(
            "ℹ️ **Help**\n\n"
            "**Available Commands:**\n"
            "• /start - Show main menu\n"
            "• /help - Show this help message\n"
            "• /menu - Show menu again\n\n"
            "**How to use:**\n"
            "Click on any button in the menu to navigate through different options.",
            parse_mode='Markdown'
        )
    elif query.data == 'contact':
        await query.edit_message_text(
            "📞 **Contact Information**\n\n"
            "• Email: support@example.com\n"
            "• Telegram: @support_bot\n"
            "• Website: https://example.com\n\n"
            "Feel free to reach out for support!",
            parse_mode='Markdown'
        )
    elif query.data == 'games':
        await query.edit_message_text(
            "🎮 **Games**\n\n"
            "• Tic Tac Toe\n"
            "• Number Guessing\n"
            "• Word Games\n"
            "• Quiz Games\n\n"
            "Game features coming soon!",
            parse_mode='Markdown'
        )
    elif query.data == 'tools':
        await query.edit_message_text(
            "🔧 **Tools**\n\n"
            "• Calculator\n"
            "• Weather Checker\n"
            "• Currency Converter\n"
            "• Reminder Setter\n\n"
            "Utility tools will be available here.",
            parse_mode='Markdown'
        )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show the main menu again."""
    await start(update, context)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await button_handler(update, context)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("help", help_command))
    
    # Add callback query handler for button presses
    application.add_handler(CallbackQueryHandler(button_handler))

    # Run the bot until the user presses Ctrl-C
    print("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
