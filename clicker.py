from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time

# loading website
driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")


def consent():
    # Consenting to cookie usage
    consent_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]")
    consent_button.click()


def choose_language():
    # Choose language
    time.sleep(2)
    language_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
    language_button.click()


def click_cookie():
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()


def list_products(element_id: str, element_class: str):
    """

    :param element_id: The larger html element containing the list of upgrades, buildings etc.
    :param element_class:  The element name needed to be extracted from element_id
    :return: a list of class names ei. "product unlocked enabled"
    """
    element_table = driver.find_element(By.ID, element_id)
    return element_table.find_elements(By.CLASS_NAME, element_class)


# wait for webpage to load
# TODO integrate explicit waits
time.sleep(5)

consent()

choose_language()
time.sleep(5)
while True:

    click_cookie()

    # clicks first upgrade to buy
    upgrades = list_products("upgrades", "upgrade")
    if upgrades:
        upgrade_details = upgrades[0].get_attribute("class")
        if "enabled" in upgrade_details:
            upgrades[0].click()

    click_cookie()

    # click to buy buildings
    building = list_products("products", "product")
    for b in building:
        building_details = b.get_attribute("class")
        if "enabled" in building_details:
            b.click()

    click_cookie()

# TODO 4. click golden cookies "shimmers"
