from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# loading website
driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

# Consenting to cookie usage
consent_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]")
consent_button.click()

# QUICK 2. Choose language
time.sleep(2)
language_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language_button.click()

# click cookie
time.sleep(2)
cookie = driver.find_element(By.ID, "bigCookie")
cookie.click()


# TODO 2. click to buy buildings
# TODO 3. click to buy upgrades
# TODO 4. click golden cookies "shimmers"
