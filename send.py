import requests
from getUpdates import get_updates
TOKEN = '6066920082:AAH3Xd8Pjt3dTVRawHehzukBcE6doUNlN8A'


def sendDocument(chat_id, document):
    params = {
        "chat_id": chat_id,
    }
    file = {
        'document': document
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

    response = requests.post(URL, params=params, files=file)
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

document = open('text.txt', 'rb')

# sendDocument(chat_id, document)
# sendContact(chat_id, '+998975787678', 'Asror', 'Bobomurodov')
# sendDice(chat_id, emoji="🎲")