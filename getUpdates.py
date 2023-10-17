import requests

def get_updates(TOKEN):
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    response = requests.get(url=BASE_URL)
    updates=response.json()
    data = updates['result'][-1]
    return data

# print(get_updates('Token here'))