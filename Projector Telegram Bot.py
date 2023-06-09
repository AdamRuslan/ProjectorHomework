import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Telegram bot token
TOKEN = '6152531269:AAGcIn30QtUa9K92j7c-kRi8ufwSkKmo0RM'


def start(update: Update, context):
    """Handler for the /start command"""
    update.message.reply_text('Welcome to the GIF search bot! Enter a search term to find GIFs.')


def search_gifs(search_term, api_key):
    url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=5"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        gif_urls = []
        for gif in data["data"]:
            gif_urls.append(gif["images"]["original"]["url"])

        return gif_urls

    except requests.exceptions.HTTPError as error:
        logger.error(f"An HTTP error occurred: {error}")
    except requests.exceptions.RequestException as error:
        logger.error(f"An error occurred: {error}")


def search(update: Update, context):
    """Handler for text messages"""
    search_term = update.message.text
    api_key = "zskeAiq9VsWRrdkayweeOAFiYnx3iKiK"
    gif_urls = search_gifs(search_term, api_key)

    if gif_urls:
        for gif_url in gif_urls:
            update.message.reply_animation(gif_url)
    else:
        update.message.reply_text("No GIFs found for the search term.")


def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search))
    # Start the bot
    updater.start_polling()
    logger.info("Bot started!")
    updater.idle()


if __name__ == "__main__":
    main()
