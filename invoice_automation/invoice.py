from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
chrome_options = Options()
## to run everything background
#chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()
driver.get('https://www.amazon.com')
sign_in_page=driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
sign_in_page.click()
