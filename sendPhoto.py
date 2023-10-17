import requests
from getUpdates import get_updates
TOKEN = 'Token here'

def sendPhoto(chat_id:str, photo:str):
    params = {
        "chat_id": chat_id,
    }
    file = {
        "photo": photo
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    response = requests.post(URL, params = params, files=file)
    return response.json()

photo = open('bot.png', 'rb')

data = get_updates(TOKEN)
chat_id = data['message']['chat']['id']


# send photo with three ways: url, id, file
sendPhoto(chat_id, photo)
