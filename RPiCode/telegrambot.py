from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from os import system

def turnon(bot,update):
    system('python switchon.py')
    print('Switched on from telegram')
	#chat_id=update.message.chat_id
	#bot.send_message(update.effective_chat.id,"Turned on light.")
	#update.message.reply_text('Light turned on!')

def turnoff(bot,update):
    system('python switchoff.py')
    print('Switched off from telegram')
        #chat_id=update.message.chat_id
        #bot.send_message(update.effective_chat.id,"Turned off light.")
	#update.message.reply_text('Light turned off!')

def main():
    updater = Updater('1476201773:AAFdr3lFeEqrLLGrNI9Qjf__tOTJ4OUPoes')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('turnon',turnon))
    dp.add_handler(CommandHandler('turnoff',turnoff))	
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
