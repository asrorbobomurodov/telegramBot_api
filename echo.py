import requests
from getUpdates import get_updates
TOKEN = '6066920082:AAH3Xd8Pjt3dTVRawHehzukBcE6doUNlN8A'

def get_dog_url():
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    return response.json()['url']

def get_cat_url():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    return response.json()[0]['url']

def sendMessage(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    button1 = {
        'text': 'Dog 🐶'
    }

    button2= {
        'text': 'Cat 😺'
    }

    keyboard = {
        'keyboard': [[button1, button2]]
    }
    params = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': keyboard
    }

    response = requests.get(url, json=params)
    return response.json()

def sendPhoto(chat_id, photo):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    params = {
        'chat_id': chat_id,
        'photo': photo
    }

    response =  requests.get(url, params=params)
    return response.json()

last_msg_id = -1
while True:
    data = get_updates(TOKEN)['message'] # last message info
    msg_id = data['message_id']
    chat_id = data['chat']['id'] 
    if last_msg_id != msg_id:
        text = data.get('text')
        photo = data.get('photo')
        if text != None:
            if text == 'Dog 🐶':
                sendPhoto(chat_id, get_dog_url())
            elif text == 'Cat 😺':
                sendPhoto(chat_id, get_cat_url())
            else:
                sendMessage(chat_id, 'Click "Dog 🐶" or "Cat 😺" button 👇')
    last_msg_id = msg_id
