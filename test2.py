import time
import threading
import requests
flag = 0
USDT_INR = float(input('usdt_inr'))
OFFSET = float(input('enter offset'))


def apiCall():
    global flag
    global USDT_INR
    global OFFSET
    while flag == 0 and (USDT_INR, OFFSET):
        result = requests.get(
            'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT').json()
        # print(result["askPrice"])
        # print({
        #     "USDT_INR": round(USDT_INR * float(result["askPrice"])),
        #     "INDEX": round(OFFSET * (USDT_INR * float(result["askPrice"])) + USDT_INR * float(result["askPrice"]))
        # })

        if flag == 1:
            time.sleep(5)
        if flag == 2:
            print("exiting")
            break


def get_input():
    global flag
    global USDT_INR
    global OFFSET
    value_usdt = float(input('Enter usdt_inr'))
    value_offset = float(input('Offset in %'))
    # off = input('do you wanna turn it off')
    # thread doesn't continue until key is pressed
    print(f'You Entered USDT_INR = {value_usdt} OFFSET = {value_offset}')
    USDT_INR = value_usdt
    OFFSET = value_offset
    if value_usdt and value_offset:
        flag = 1
    print('flag is now:', flag)


n = threading.Thread(target=apiCall)
i = threading.Thread(target=get_input)
if (USDT_INR, OFFSET):
    n.start()
    i.start()
else:
    print("Enter the values")
