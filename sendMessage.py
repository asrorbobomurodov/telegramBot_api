import os
import requests

TOKEN = '6388893107:AAGIbsoNExuuEgRirNnCbLQyN_wI9-9BrPA'

def sendMessage(chat_id:str, text:str):
    params = {
        "chat_id":chat_id,
        "text": text
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    response = requests.get(URL, params=params)

    return response.status_code
    
chat_id = 5575549228
text = "hi"
print(sendMessage(chat_id, text))
