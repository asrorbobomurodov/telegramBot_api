import requests
TOKEN="6066920082:AAH3Xd8Pjt3dTVRawHehzukBcE6doUNlN8A"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)

updates = response.json()

data = updates['result'][-1]

# chat_id = data['message']['chat']['id']
print(data)