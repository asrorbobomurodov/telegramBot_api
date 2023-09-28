import os
import requests

TOKEN='6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY'

def sendMessage(chat_id:str, text:str):
    button1 = {
        "text": "Button1",
        "request_contact": True
    }
    button2 = {
        "text": "Button2"
    }
    button3 = {
        "text": "Button3"
    }
    keyboard = {"keyboard": [[button1, button2], [button3]], "resize_keyboard": True}

    params = {
        "chat_id":chat_id,
        "text": text,
        "reply_markup": keyboard
    }
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(url, json=params)

    return response.json()

chat_id = 5575549228
text = "hi"
print(sendMessage(chat_id, text))
