import requests
import time
import pygame

def get_bicoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']


# print(get_bicoin_price())

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('la-ele-manoel-gomes.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def monitor_price(threshold=100, tolerance=50):
    prev_price = get_bicoin_price()

    while True:
        price = get_bicoin_price()
        print(f'Current price: {price}')
        if price > prev_price + threshold:
            print('Price increased!')
            play_sound()
        elif price < prev_price - threshold:
            print('Price decreased!')
            play_sound()
        prev_price = price
        time.sleep(tolerance)

monitor_price()