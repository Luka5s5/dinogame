# Telegram Bot for Game Access

This bot checks if a user is subscribed to a specific Telegram channel and provides access to a game based on their subscription status.

## Setup

1. Create a new bot with [@BotFather](https://t.me/BotFather) and get your bot token
2. Add the bot to your channel as an administrator
3. Clone this repository
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

## Configuration

Edit the `bot.py` file to update:
- `CHANNEL_ID`: The username of your channel (with @)
- `BOT_USERNAME`: The username of your bot (without @)

## Running the Bot

```bash
python bot.py
```

## How it Works

- When a user sends `/start` or any message to the bot:
  - If they are subscribed to the channel, the bot sends them the game link
  - If they are not subscribed, the bot sends them the channel link to subscribe

## Dependencies

- python-telegram-bot==13.7
- python-dotenv==0.19.0