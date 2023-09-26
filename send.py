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

document = 'BQACAgIAAxkBAAIBO2US2m3ZhtnV_yKll4mOna1ftX3wAALBNAAClx2QSMymeSz6F6twMAQ'

data = get_updates(TOKEN)
chat_id = data['message']['chat']['id']

sendDocument(chat_id, document)

