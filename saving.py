import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def creating_save_file(save_text, file_name):
    with open("save_file\\" + file_name + ".txt", "w") as save_file:
        save_file.write(save_text)


def fetching_save_file():
    list_of_files = glob.glob("save_file/*.txt")
    if list_of_files:
        with open(list_of_files[0], "r") as save_file:
            return save_file.readlines()[0]


def go_to_options(web_driver):
    if web_driver.find_element(By.ID, "menu").is_displayed():
        menu = web_driver.find_element(By.ID, "menu")
        subsection = menu.find_element(By.CLASS_NAME, "subsection")
        buttons = subsection.find_elements(By.CSS_SELECTOR, "a")
        return buttons
    else:
        options_button = web_driver.find_element(By.ID, "prefsButton")
        options_button.click()
        menu = web_driver.find_element(By.ID, "menu")
        subsection = menu.find_element(By.CLASS_NAME, "subsection")
        buttons = subsection.find_elements(By.CSS_SELECTOR, "a")
        return buttons


def exporting_save_file(web_driver):
    # TODO CHECK HOW LONG THE LIST OF BUTTONS ARE. THE REASON FOR THIS IS IF GIFTING IS PRESENT THEN THE LIST IS LONGER
    # TODO CONT. AND IF ITS LONGER THAN THIS FUNCTION WON'T BE ABLE TO EXPORT SAVE FILE
    buttons = go_to_options(web_driver)
    # buttons[2].click() # previously used, before finding "present bug"
    buttons[4].click()  # export save button
    export_prompt = web_driver.find_element(By.ID, "textareaPrompt")
    export_text = export_prompt.text
    export_prompt.send_keys(Keys.ENTER)
    return export_text


# Load save file
def importing_save_file(web_driver, lines):
    buttons = go_to_options(web_driver)
    buttons[3].click()  # import save button
    import_save = web_driver.find_element(By.ID, "textareaPrompt")
    import_save.send_keys(lines)
    import_save.send_keys(Keys.ENTER)

