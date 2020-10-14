import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hello {}'.format(
        update.message.from_user.first_name))


def help(update, context):
    update.message.reply_text('Message @wistic')


def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(
        os.environ['TELEGRAM_API_TOKEN'], use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
