import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a Telegram bot!")

def main():
    updater = Updater(token=os.environ['TELEGRAM_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()

if __name__ == '__main__':
    main()
