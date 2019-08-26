import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from string_utils import i_replace, upper_lower, dumb_text

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
    bot.send_message(chat_id=update.message.chat_id, text=i_replace(update.message.text))


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def distort(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text=upper_lower(' '.join(args)))


def dumb(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text=dumb_text(args))


def dumb2(bot, update, args):
    bot.send_message(chat_id=update.message.chat_id, text=upper_lower(dumb_text(args)))


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('caps', caps, pass_args=True))
    dispatcher.add_handler(CommandHandler('distort', distort, pass_args=True))
    dispatcher.add_handler(CommandHandler('dumb', dumb, pass_args=True))
    dispatcher.add_handler(CommandHandler('dumb2', dumb2, pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
