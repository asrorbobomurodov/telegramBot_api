import requests

TOKEN = '6066920082:AAH3Xd8Pjt3dTVRawHehzukBcE6doUNlN8A'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'


response = requests.get(url=BASE_URL)
if response.status_code == 200:
    info = response.json()
    print(info)