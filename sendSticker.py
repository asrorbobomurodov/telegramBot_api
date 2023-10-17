import requests
from getUpdates import get_updates

def sendSticker(chat_id, sticker):
    url = "https://api.telegram.org/bot6431620392:AAFur8ALeq6cKizXogjt3oM1deR9RVOsLpk/sendSticker"

    params = {
        "chat_id": chat_id,
        "sticker": sticker
    }

    response = requests.get(url, params=params)
    return response.json

msg = get_updates('6431620392:AAFur8ALeq6cKizXogjt3oM1deR9RVOsLpk')['message']
chat_id = msg['chat']['id']
sticker = msg['sticker']['file_id']

sendSticker(chat_id, sticker=sticker)

# print(chat_id)