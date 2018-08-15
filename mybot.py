import requests
import datetime
from time import sleep

class BotHandler:
	def __init__(self, token):
		self.token = token
		self.api_url = "https://api.telegram.org/bot{}/".format(token)

	def get_updates(self, offset = None, timeout = 30):
		method = 'getUpdates'
		params = {'timeout': timeout, 'offset': offset}
		response = requests.get(self.api_url + method, data = params)
		result_json = response.json()['result']
		return result_json

	def get_last_update(self):
		get_result = self.get_updates()
		print("Length of get_result {}".format(len(get_result)))
		if len(get_result) > 0:
			last_update = get_result[-1]
		else:
			last_update = get_result[len(get_result)]
		return last_update


	def get_chat_id(self, update):
		chat_id = update['message']['chat']['id']
		return chat_id

	def send_message(self, chat_id, text):
		params = {'chat_id': chat_id, 'text': text}
		method = 'sendMessage'
		response = requests.post(self.api_url + method, data = params)
		return response



token = "605512380:AAHGR3qTbUWPfqEYiXePq0NZbSaxvXjbNJQ"
greet_bot = BotHandler(token)
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()

def main():
	new_offset = None
	today = now.day
	hour = now.hour

	while True:
		print("Billa {}".format(new_offset))
		greet_bot.get_updates(new_offset)

		last_update = greet_bot.get_last_update()

		last_update_id = last_update['update_id']

		last_chat_text = last_update['message']['text']

		last_chat_id = last_update['message']['chat']['id']

		last_chat_name = last_update['message']['chat']['first_name']

		print("{} - Billa  {}".format(last_update_id, last_chat_text))
		if last_chat_text.lower() in greetings  and 6 <= hour < 12:
			greet_bot.send_message(last_chat_id, 'Good Morning{}'.format(last_chat_name))
			today += 1
		elif last_chat_text.lower() in greetings  and 12 <= hour < 17:
			greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
			today += 1
		elif last_chat_text.lower() in greetings  and 17 <= hour < 23:
			greet_bot.send_message(last_chat_id, 'Good Evening {}'.format(last_chat_name))
			today += 1

		new_offset = last_update_id + 1
		print(new_offset)
		print("")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()



'''def main():
	update_id = last_update(get_updates_json(url))['update_id']
	while True:
		print("{} == {}".format(update_id, last_update(get_updates_json(url))['update_id']))
		if update_id == last_update(get_updates_json(url))['update_id']:
			send_mess(get_chat_id(last_update(get_updates_json(url))),'you suck')
			update_id += 1
			sleep(1)

if __name__ == '__main__':
	main()

'''