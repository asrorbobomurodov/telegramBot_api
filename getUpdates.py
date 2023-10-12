import requests

def get_updates(TOKEN):
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url=BASE_URL)
    updates=response.json()
    data = updates['result'][-1]
    return data

print(get_updates('6066920082:AAH3Xd8Pjt3dTVRawHehzukBcE6doUNlN8A'))