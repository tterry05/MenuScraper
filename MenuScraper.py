from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pushbullet import Pushbullet
from Methods import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['API']['key']

pb = Pushbullet(api_key)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://portal.uwplatt.edu/dining-menu")

lunchmenu(driver)
food = getmenu(driver)

message = ""
for msg in food:
    message += msg + "\n"

push = pb.push_note("Food", message)

driver.quit()
