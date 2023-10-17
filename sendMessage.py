import os
import requests
from getUpdates import get_updates

TOKEN = 'Token here'

def sendMessage(chat_id:str, text:str):
    params = {
        "chat_id":chat_id,
        "text": text
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(URL, params=params)

    return response.json()

updates = get_updates(TOKEN)
chat_id = updates['message']['chat']['id']
text = updates['message']['text']
sendMessage(chat_id, text)
