from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from saving import fetching_save_file, importing_save_file, exporting_save_file, creating_save_file
from timer import starting_time, back_up_time
import re


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
        click_golden_cookie()  # to check for golden cookie if it obscures the big cookie
        cookie.click()


def click_golden_cookie():
    # click golden cookies
    shimmer = driver.find_elements(By.CLASS_NAME, "shimmer")
    if shimmer:
        for golden in shimmer:
            golden.click()


def list_products(element_id: str, element_class: str):
    """
    :param element_id: The larger html element containing the list of upgrades, buildings etc.
    :param element_class:  The element name needed to be extracted from element_id
    :return: a list of class names ei. "product unlocked enabled"
    """
    element_table = driver.find_element(By.ID, element_id)
    return element_table.find_elements(By.CLASS_NAME, element_class)


def text_cleaner(text):
    # finding text this way is not guranteed, as there are two word buildings in game
    search_obj = re.search(r"\((.+)%", text)
    try:
        percentage_text = search_obj.group(1)
    except AttributeError:
        percentage_text ="0.0"
        print(text)
    bad_char = ("(", "%")
    for c in bad_char:
        new_text = percentage_text.replace(c, "")
    return float(new_text)


# wait for webpage to load
# TODO integrate explicit waits
time.sleep(5)

consent()
choose_language()

time.sleep(5)

save_file_text = fetching_save_file()
importing_save_file(driver, save_file_text)
time.sleep(1)

time_to_backup = 100
now = datetime.datetime.now()
backup_timer = back_up_time(now, time_to_backup)

while True:
    click_cookie(10)
    current_time = starting_time()
    if current_time >= backup_timer:
        back_up_save_text = exporting_save_file(driver)
        creating_save_file(back_up_save_text, "save file")
        print(f"updated at {current_time}")
        backup_timer = back_up_time(datetime.datetime.now(), time_to_backup)
    # TODO 1.  scroll buildings list and upgrades list into view
    # TODO 2.ask user for parameters before running the bot to automate building buying and upgrade buying etc.

    # # clicks first upgrade to buy
    # upgrades = list_products("upgrades", "upgrade")
    # if upgrades:
    #     upgrade_details = upgrades[0].get_attribute("class")
    #     if "enabled" in upgrade_details:
    #         upgrades[0].click()
    #
    # # click to buy buildings
    # building = list_products("products", "product")
    # building_to_click = ("", 0)
    # for b in building[::-1]:
    #     building_details = b.get_attribute("class")
    #     if "enabled" in building_details:
    #         hover = ActionChains(driver).move_to_element(b)
    #         hover.perform()
    #         building_description = driver.find_elements(By.CLASS_NAME, "descriptionBlock")
    #         if building_description:
    #             building_description_text = building_description[1].text
    #             building_profit_per = text_cleaner(building_description_text)
    #
    #             if building_profit_per >= building_to_click[1]:
    #                 # PROBLEM WITH THIS APPROACH IS THAT IT WON'T SELECT THE 0 BUILDING
    #                 building_to_click = (b, building_profit_per)
    # if building_to_click[1] != 0:
    #     building_to_click[0].click()



