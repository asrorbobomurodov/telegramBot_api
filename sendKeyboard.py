from getUpdates import get_updates
import requests
from time import sleep

TOKEN='6431620392:AAFur8ALeq6cKizXogjt3oM1deR9RVOsLpk'

def sendMessage(chat_id:str, text:str):
    button1 = {
        "text": "Dog 🐶"
    }
    button2 = {
        "text": "Cat 😺"
    }

    keyboard = {
        'keyboard': [[button1, button2]],
        'resize_keyboard': True,
        'input_field_placeholder': 'Click button Asror'
    }
    params = {
        "chat_id":chat_id,
        "text": text,
        "reply_markup": keyboard
    }
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(url, json=params)

    return response.json()

last_msg_id = -1
while True:
    data = get_updates(TOKEN)['message']
    msg_id = data['message_id']
    chat_id = data['chat']['id']
    text = data.get('text')
    if last_msg_id != msg_id:
        if text == '/start':
            sendMessage(chat_id, 'Welcome to "EchoBot"')
        elif text != None:
            sendMessage(chat_id, text)
        
    last_msg_id = msg_id
    sleep(1)