import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r'C:/Users/YourUserName/YourDriverPath'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://10parmak.girisim.dev/')

time.sleep(1)

start = driver.find_element("id", "start-btn")
start.click()

time.sleep(2)

while True:
    try:
        element = driver.find_element(By.CSS_SELECTOR, "span.word.current")
        input_box = driver.find_element(By.ID, "word-input")
        input_box.send_keys(element.text + " ")

        time.sleep(0.2)
    except Exception:
        break

