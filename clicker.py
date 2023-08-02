from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# TODO QUICK 1. Consent to cookie usage, Switch to iframe
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]")
# TODO QUICK 2. Choose language
# TODO 1. click cookie
cookie = driver.find_element(By.ID, "bigCookie")
cookie.click()


# TODO 2. click to buy buildings
# TODO 3. click to buy upgrades
# TODO 4. click golden cookies "shimmers"
