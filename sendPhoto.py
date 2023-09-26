import os 
import requests
from getUpdates import get_updates
TOKEN = '6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY'

def sendPhoto(chat_id:str,photo:str):
    params = {
        "chat_id": chat_id,
        "photo": photo
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    response = requests.get(URL, params = params)
    return response.json()


photo_url='https://miro.medium.com/v2/resize:fit:300/1*YVTFl1UEkt3_rkez-DIU9w.png'

data = get_updates(TOKEN)
chat_id = data['message']['chat']['id']

# send photo with three ways: url, id, file
sendPhoto(chat_id, photo_url)
