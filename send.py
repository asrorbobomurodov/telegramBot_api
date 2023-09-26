import os 
import requests
from getUpdates import get_updates
TOKEN = '6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY'


def sendDocument(chat_id, document):
    params = {
        "chat_id": chat_id,
        "document": document
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

    response = requests.post(URL, params=params)
    return response.json()

def sendContact(chat_id, phone_number, first_name, last_name=None):
    params = {
        "chat_id": chat_id,
        "phone_number": phone_number,
        "first_name": first_name,
        "last_name": last_name
    }

    URL = f'https://api.telegram.org/bot{TOKEN}/sendContact'

    response = requests.post(URL, params=params)
    return response.json()

def sendDice(chat_id, emoji=None):
    params = {
        "chat_id": chat_id,
        "emoji": emoji
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDice'

    response = requests.post(URL, params=params)
    return response.json()

data = get_updates(TOKEN)
chat_id = data['message']['chat']['id']

sendDice(chat_id, emoji="⚽")