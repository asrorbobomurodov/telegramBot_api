import requests

TOKEN = ''
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


response = requests.get(url=BASE_URL)
updates=response.json()['result']
data = updates['result'][-1]
chat_id = data['message']['chat']['id']
# print each update
