import requests
import json
import sys

class Api:
	def __init__(self):
		self.url = "https://solved.ac/api/v3/user/show?handle={}"

	
	def get_search_user(self, user_name):
		payload = ""
		headers = {}
		response = requests.request("GET", self.url.format(user_name), headers=headers, data=payload)

		return json.loads(response.text)
