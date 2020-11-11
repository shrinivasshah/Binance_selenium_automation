import requests
import time

flag = 0
USDT_INR = float(input('Enter usdt_inr: '))
OFFSET = float(input('Enter offset: '))
UPPER_LIMIT = int(input("Enter upper lim"))
LOWER_LIMIT = int(input("Enter lower lim"))

# result = requests.get(
#     'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT')
# print(result.content)
# tricker_on = False

while True:
    result = requests.get(
        'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT').json()
    index_price = round(
        OFFSET * (USDT_INR * float(result["askPrice"])) + USDT_INR * float(result["askPrice"]))

    if int(index_price) in range(LOWER_LIMIT, UPPER_LIMIT):
        # print(result["askPrice"])
        print({
            # "USDT_INR": round(USDT_INR * float(result["askPrice"])),
            "INDEX": index_price
        })
    else:
        print('Not in range')
