import glob
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def creating_save_file(save_text):
    with open("save_file.txt", "w") as save_file:
        save_file.write(save_text)


def fetching_save_file():
    list_of_files = glob.glob("save_file/*.txt")
    if list_of_files:
        with open(list_of_files[0], "r") as save_file:
            return save_file.readlines()[0]

# TODO 2. Create save file


def exporting_save_file(web_driver):
    options_button = web_driver.find_element(By.ID, "prefsButton")
    options_button.click()
    menu = web_driver.find_element(By.ID, "menu")
    subsection = menu.find_element(By.CLASS_NAME, "subsection")
    buttons = subsection.find_elements(By.CSS_SELECTOR, "a")
    buttons[2].click()  # export save button
    export_prompt = web_driver.find_element(By.ID, "textareaPrompt")
    export_text = export_prompt.text
    export_prompt.send_keys(Keys.ENTER)
    return export_text


# Load save file
def importing_save_file(web_driver, lines):
    options_button = web_driver.find_element(By.ID, "prefsButton")
    options_button.click()
    menu = web_driver.find_element(By.ID, "menu")
    subsection = menu.find_element(By.CLASS_NAME, "subsection")
    buttons = subsection.find_elements(By.CSS_SELECTOR, "a")
    buttons[3].click()  # import save button
    import_save = web_driver.find_element(By.ID, "textareaPrompt")
    import_save.send_keys(lines)
    import_save.send_keys(Keys.ENTER)

