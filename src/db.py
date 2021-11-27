import requests
import os
import sys
import pymysql

class Db:
	def __init__(self):
		dakdalbot_pw = os.environ['dakdalbot_pw']
		self.conn = pymysql.connect(host='localhost', user='dakdalbot' , password=dakdalbot_pw, db='dakdaldb', charset='utf8')
		self.cursor = self.conn.cursor() 

		sql = '''CREATE TABLE IF NOT EXISTS user ( 
				id					int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
				user_id			varchar(255), 
				telegram_id varchar(255),
				solved			int(11),
				tier				int(11),
				ranking			int(11)
				)
		''' 

		self.cursor.execute(sql) 

		self.conn.commit() 

	def get_all_user(self):
		sql = '''SELECT * FROM user'''
		self.cursor.execute(sql)
		return self.cursor.fetchall()
	
	def add_user(self, user_dict):
		sql = '''INSERT INTO user (user_id, telegram_id, solved, tier, ranking) 
		VALUES ('{}', '{}', {}, {}, {})
		'''.format(
				user_dict['user_id'], 
				user_dict['telegram_id'], 
				user_dict['solved'], 
				user_dict['tier'], 
				user_dict['ranking']
				)
		self.cursor.execute(sql)
		self.conn.commit()
	
	def update_user(self, user_id, solved, tier, ranking):
		sql = '''UPDATE user
		SET solved={}, tier={}, ranking={}
		WHERE user_id='{}'
		'''.format(solved, tier, ranking, user_id)
		self.cursor.execute(sql)
		self.conn.commit()
