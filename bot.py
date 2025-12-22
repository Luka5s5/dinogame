import logging
import os

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters, CallbackQueryHandler)

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Channel and bot information
CHANNEL_ID = "@zaart_community"  # Replace with your channel username
BOT_USERNAME = "cultural_worker_bot"  # Replace with your bot username (without @)
GAME_URL = f"https://t.me/{BOT_USERNAME}/game"  # Game URL for the bot

MESSAGE_NOT_SUBSCRIBED = """Привет, это команда «ЗА АРТ»!

Под новый год, мы сделали игру, где можно закрывать горящие дедлайны и отчеты в один клик. Собирай оливьешку и подарки от Деда Мороза, чтобы победить все дела. А если игра кончится, то всегда можно начать с начала. 

Закрывать задачи одним прыжком могут только подписчики телеграм-канала https://t.me/zaart_community, в котором мы рассказываем, как создаем культурные проекты."""

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE, user_id: int) -> bool:
    """
    Check if user is subscribed to the channel
    """
    try:
        # Get chat member status
        chat_member = await context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        
        # Check if user is a member or administrator (not restricted, kicked, etc.)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        logger.error(f"Error checking subscription: {e}")
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the appropriate link based on subscription status."""
    await handle_message(update, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle all other messages by checking subscription status."""
    user_id = update.effective_user.id
    
    # Check if user is subscribed to the channel
    is_subscribed = await check_subscription(update, context, user_id)
    
    if is_subscribed:
        # User is subscribed, send the game link
        message = f"""Привет, это команда «ЗА АРТ»!

Под новый год, мы сделали игру, где можно закрывать горящие дедлайны и отчеты в один клик. Собирай оливьешку и подарки от Деда Мороза, чтобы победить все дела. А если игра кончится, то всегда можно начать с начала. 

{GAME_URL}"""
        await update.message.reply_text(message)
    else:
        # User is not subscribed, send the channel link with a check subscription button
        keyboard = [[InlineKeyboardButton("Проверить подписку", callback_data="check_subscription")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = MESSAGE_NOT_SUBSCRIBED
        await update.message.reply_text(message, reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    # Check if user is now subscribed
    is_subscribed = await check_subscription(update, context, user_id)
    
    if is_subscribed:
        # User is now subscribed, send the game link
        message = f"""Привет, это команда «ЗА АРТ»!

Под новый год, мы сделали игру, где можно закрывать горящие дедлайны и отчеты в один клик. Собирай оливьешку и подарки от Деда Мороза, чтобы победить все дела. А если игра кончится, то всегда можно начать с начала. 

{GAME_URL}"""
        await query.edit_message_text(text=message)
    else:
        # User is still not subscribed
        keyboard = [[InlineKeyboardButton("Проверить подписку", callback_data="check_subscription")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=MESSAGE_NOT_SUBSCRIBED,
            reply_markup=reply_markup
        )

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button))
    
    # Start the Bot
    application.run_polling()
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    logger.info("Bot is running...")

if __name__ == '__main__':
    main()
