from selenium.webdriver.common.by import By
import time


def clickmenu(name, driver):
    if isinstance(name, str):
        items = driver.find_elements(By.TAG_NAME, value="Option")
        for item in items:
            if item.text == name:
                item.click()
                time.sleep(1)
    else:
        items = driver.find_elements(By.TAG_NAME, value="Option")
        for item in items:
            day = item.text
            if len(day) > 0:
                day = day.split()[0]
            if day in name:
                item.click()
                time.sleep(1)
                return


# Navigates to the lunch menu for Markee for the closest weekday
def lunchmenu(driver):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    clickmenu(days, driver)
    clickmenu("Pioneer Crossing", driver)
    clickmenu("Lunch", driver)


def getmenu(driver):
    food = []
    items = driver.find_elements(By.TAG_NAME, value="Td")
    i = 0
    DuJour = 0
    Asian = 0
    while i < len(items):
        if items[i].text == "DuJour" and DuJour < 2:
            food.append(items[i + 1].text)
            DuJour += 1
        if items[i].text == "Asian Wok" and Asian < 2:
            food.append(items[i + 1].text)
            Asian += 1
        i += 1
        if Asian == 2 and DuJour == 2:
            break
    return food
