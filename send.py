import os 
import requests
from getUpdates import get_updates
TOKEN = '6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY'


def sendDocument(chat_id, document):
    params = {
        "chat_id": chat_id
    }
    file = {
        "document": document
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

    response = requests.post(URL, params=params, files=file)
    return response.json()

document = open('requirements.txt', 'r')

data = get_updates(TOKEN)
chat_id = data['message']['chat']['id']

sendDocument(chat_id, document)

