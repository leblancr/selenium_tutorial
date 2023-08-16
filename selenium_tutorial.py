from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)
chrome_binary_path = "./chrome/linux-116.0.5845.96/chrome-wrapper"
options.binary_location = chrome_binary_path

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install(),
                                          options=options))

driver.get('http://www.neuralnine.com/')
driver.maximize_window()

links = driver.find_elements('xpath', '//a[@href]')

for link in links:
    if 'Books' in link.get_attribute('innerHTML'):
        print(link.get_attribute('innerHTML'))
        link.click()
        break

time.sleep(3)