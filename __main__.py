from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

try:
    from config import TOKEN
except:
    import os
    TOKEN = os.environ.get('TOKEN')


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hili!")


def error(bot, update, error):
    logger.warning('Update: "%s" - Error: "%s"' % (update, error))


def echo(bot, update):
    new_text = update.message.text
    for letter in 'aáAeéEoóOuúU':
        new_text = new_text.replace(letter, 'i')
    bot.send_message(chat_id=update.message.chat_id, text=new_text)


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
