import os 
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', '8443'))
now = datetime.now()
strNow = now.strftime("%d/%m/%Y %H:%M:%S")

def start(update, context):
    update.message.reply_text('Hi!')

def echo(update, context):
    update.message.reply_text(update.message.text)


def main():

    TOKEN = '5706692876:AAH4koty82x0uwJtc5Pq9whVFDrM6RunQjc'
    APP_NAME = 'https://telegram123beta.herokuapp.com/'

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path = TOKEN, webhook_url=APP_NAME+ TOKEN)
    updater.idle()
   

if __name__ == '__main__':
    main()