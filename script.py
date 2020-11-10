import requests
import time


result = requests.get(
    'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT')
print(result.content)
tricker_on = False

while tricker_on:
    result = requests.get(
        'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT')
    print(result)
