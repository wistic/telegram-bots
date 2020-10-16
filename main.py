import logging
import codext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

from utility import getphoto

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hello {}'.format(
        update.message.from_user.first_name))


def help(update, context):
    update.message.reply_text('Message @wistic')


def echo(update, context):
    update.message.reply_text(update.message.text)


def leet(update, context):
    message = update.message.text.split(' ', 1)
    if len(message) == 1:
        update.message.reply_text(
            'Proper usage:\n{} argument'.format(message[0]))
    else:
        update.message.reply_text(codext.encode(message[1], 'leetspeak'))


def photo(update, context):
    message = update.message.text.split(' ', 1)
    if len(message) == 1:
        update.message.reply_text(
            'Proper usage:\n{} argument'.format(message[0]))
    else:
        url = getphoto(message[1])
        if url == 'Error':
            update.message.reply_text('Sorry not found')
        else:
            update.message.reply_text(url)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(
        os.environ['TELEGRAM_API_TOKEN'], use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('leet', leet))
    dp.add_handler(CommandHandler('photo', photo))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
