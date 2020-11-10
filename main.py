from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://techwithtim.net')
print(driver.title)
button = driver.find_element_by_class_name(
    'ow-icon-placement-right')
button.send_keys(Keys.RETURN)
