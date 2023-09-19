import requests
TOKEN="6388893107:AAGIbsoNExuuEgRirNnCbLQyN_wI9-9BrPA"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)

updates = response.json()

data = updates['result'][-1]

chat_id = data['message']['chat']['id']
print(chat_id)