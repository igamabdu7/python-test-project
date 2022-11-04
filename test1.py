import telebot.ext
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', '8443'))

def start(update, context):
    update.message.reply_text('HI!')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():

    TOKEN = '5706692876:AAH4koty82x0uwJtc5Pq9whVFDrM6RunQjc'
    APP_NAME = 'https://telegrambeta1.herokuapp.com/'

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path = TOKEN, webhook_url=APP_NAME+ TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()