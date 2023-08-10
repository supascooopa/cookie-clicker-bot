from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from saving import fetching_save_file, importing_save_file
from selenium.webdriver.support import expected_conditions as EC

# loading website
driver = webdriver.Firefox()
driver.maximize_window()
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


def click_cookie(click_amount: int = 1):
    cookie = driver.find_element(By.ID, "bigCookie")
    for click in range(click_amount):
        cookie.click()


def click_golden_cookie():
    # click golden cookies
    if EC.element_to_be_clickable((By.ID, "shimmers")):
        driver.find_element(By.ID, "shimmers").click()


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

save_file_text = fetching_save_file()
importing_save_file(driver, save_file_text)

while True:

    # click_golden_cookie()
    click_cookie()

    # clicks first upgrade to buy
    upgrades = list_products("upgrades", "upgrade")
    if upgrades:
        upgrade_details = upgrades[0].get_attribute("class")
        if "enabled" in upgrade_details:
            upgrades[0].click()


    # click to buy buildings
    building = list_products("products", "product")
    for b in building:
        building_details = b.get_attribute("class")
        if "enabled" in building_details:
            b.click()



