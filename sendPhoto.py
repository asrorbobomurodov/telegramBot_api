import os 
import requests
from getUpdates import get_updates
TOKEN = '6388893107:AAHm55DuPheZmctXz5mX5HnSfD9zfgmpNhY'

def sendPhoto(chat_id:str,photo:str):
    params = {
        "chat_id": chat_id,
    }
    file = {
        "photo":photo
    }
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'

    response = requests.post(URL, params = params, files=file)
    return response.json()


# photo_url='https://miro.medium.com/v2/resize:fit:300/1*YVTFl1UEkt3_rkez-DIU9w.png'
# file_id = 'AgACAgIAAxkBAAIBNGUS0WLd7IBg9Dt6kh8UDlG-zg-PAAL6zDEblx2QSM_jdc2XZAi1AQADAgADcwADMAQ'
photo = open('bot.png', 'rb')

data = get_updates(TOKEN)
chat_id = data['message']['chat']['id']


# send photo with three ways: url, id, file
sendPhoto(chat_id, photo)
