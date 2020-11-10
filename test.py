import time
import threading
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# set global variable flag

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://pbtestadmin.onerooftechnologies.com')
print(driver.title)
time.sleep(30)
driver.get('http://pbtestadmin.onerooftechnologies.com/BuyAndSellingRate/Index')


flag = 0
USDT_INR = float(input('Enter usdt_inr: '))
OFFSET = float(input('Enter offset: '))


def apiCall():
    global flag
    global USDT_INR
    global OFFSET
    while flag == 0 or flag == 1 and (USDT_INR, OFFSET):
        result = requests.get(
            'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT').json()
        # print(result["askPrice"])
        # print({
        #     "USDT_INR": round(USDT_INR * float(result["askPrice"])),
        #     "INDEX": round(OFFSET * (USDT_INR * float(result["askPrice"])) + USDT_INR * float(result["askPrice"]))
        # })
        try:

            input_Field = driver.find_element_by_xpath(".//*[@id='txtRate']")
            action_chains = ActionChains(driver)
            action_chains.double_click(input_Field).perform()
            input_Field.send_keys(round(
                OFFSET * (USDT_INR * float(result["askPrice"])) + USDT_INR * float(result["askPrice"])))

        finally:
            submit_button = driver.find_element_by_xpath(
                '//*[@id="btnupdateRateEnginRate"]')
            submit_button.click()
            time.sleep(0.7)
            confirm_button = driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/button[2]')
            confirm_button.click()
            time.sleep(0.7)
            submit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[4]/div/div/div[1]/button'))
            )
            submit_button.click()

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
    value_offset = float(input('Enter offset: '))
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


# def apiCall():
#     global flag
#     global USDT_INR
#     global OFFSET
#     while flag == 0 and (USDT_INR, OFFSET):
#         result = requests.get(
#             'https://api.binance.com/api/v3/ticker/bookTicker?symbol=BTCUSDT')

#         time.sleep(2)
#         if flag == 1:
#             time.sleep(5)
#         if flag == 2:
#             print("exiting")
#             break


# def get_input():
#     global flag
#     global USDT_INR
#     global OFFSET
#     value_usdt = float(input('Enter usdt_inr'))
#     value_offset = float(input('Offset in %'))
#     off = input('do you wanna turn it off')
#     # thread doesn't continue until key is pressed
#     print(f'You Entered USDT_INR = {value_usdt} OFFSET = {value_offset}')
#     USDT_INR = value_usdt
#     OFFSET = value_offset
#     if value_usdt and value_offset:
#         flag = 1
#     if off:
#         flag = 2
#     print('flag is now:', flag)


# n = threading.Thread(target=apiCall)
# i = threading.Thread(target=get_input)
# n.start()
# i.start()
