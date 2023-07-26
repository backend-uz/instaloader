from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import start, text

TOKEN = '2116227480:AAF9ftaJfTSu7hRsaePI-gCxmOgzlGtMGxk'

def main():
    updater = Updater(token=TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()