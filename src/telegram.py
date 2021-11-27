import requests
import telegram
import json
import os

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

class Telegram:
	def __init__(self):
		my_token = os.environ['token']
		self.bot = telegram.Bot(token=my_token)
		self.updater = Updater(token=my_token, use_context=True)

	def get_message(self):
		updates = self.bot.getUpdates()
		return updates[-1]
#		for u in updates:
#			print(u.message)
	
	def send_message(self, telegram_id, message):
		self.bot.sendMessage(chat_id=telegram_id, text=message)

	def telegram_updater(self, method):
		dispatcher = self.updater.dispatcher
		echo_handler = MessageHandler(Filters.text & (~Filters.command), method)
		dispatcher.add_handler(echo_handler)

		self.updater.start_polling()
