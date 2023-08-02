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
while True:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()

    # click to buy buildings
    buildings_list = driver.find_element(By.ID, "products")
    building = buildings_list.find_elements(By.CLASS_NAME, "product")
    for b in building:
        building_details = b.get_attribute("class")
        if "enabled" in building_details:
            b.click()
        # print(building_details)
    cookie.click()

    # click to buy upgrades
    upgrades_list = driver.find_element(By.ID, "upgrades")
    upgrades = upgrades_list.find_elements(By.CLASS_NAME, "upgrade")
    for u in upgrades:
        upgrade_details = u.get_attribute("class")
        if "enabled" in upgrade_details:
            u.click()
# TODO 4. click golden cookies "shimmers"
