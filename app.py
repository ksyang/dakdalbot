import threading
import time
from src.api import Api
from src.db import Db
from src.telegram import Telegram

USER_ID = 1
TELEGRAM_ID = 2
SOLVED = 3
TIER = 4
RANKING = 5
db				= Db()
api				= Api()
telegram = Telegram()

def dakdal():
	prior_solved = 0 # DB에서 가져와야 함
	while True:
		time.sleep(10800)
		all_user = db.get_all_user()
		for user in all_user:
			user_data = api.get_search_user(user[USER_ID])
			if user[SOLVED] != user_data['solvedCount']:
				db.update_user(
						user[USER_ID],
						user_data['solvedCount'], 
						user_data['tier'],
						user_data['rank'],
						)
			else:
				for _ in range(3):
					print('{} get message.'.format(user[USER_ID]))
					telegram.send_message(user[TELEGRAM_ID], '문제 안 푼지 벌써 3시간이 초과되었습니다. 어서 문제 푸세요.')

def addUser():
	telegram.telegram_updater(updateUser)

def updateUser(update, context):
	user_id = update.message.text
	telegram_id = update.effective_chat.id
	user_data = api.get_search_user(user_id)

	db.add_user({'user_id': user_id,
			'telegram_id': telegram_id,
			'solved': user_data['solvedCount'],
			'tier': user_data['tier'],
			'ranking': user_data['rank']
			})


'''	db				= Db()
	api				= Api()
	while True:
		msg = 
		print(msg)
		if msg == None: continue
		user_id = msg['message']['text']
		telegram_id = msg['message']['chat']['id']
		user_data = api.get_search_user(user_id)

		db.add_user({'user_id': user_id,
				'telegram_id': telegram_id,
				'solved': user_data['solvedCount'],
				'tier': user_data['tier'],
				'ranking': user_data['rank']
				})

		time.sleep(1)
	'''

if __name__=="__main__":
	t = threading.Thread(target=dakdal)
	t2 = threading.Thread(target=addUser)
	t.start()
	t2.start()	

# 921613115


#		db = Db()
#		user_dict = {'user_id':'user',
#			'telegram_id':'tel',
#			'solved':892,
#			'tier':1,
#			'ranking':892}
#		db.add_user(user_dict)
#		db.get_all_user()

