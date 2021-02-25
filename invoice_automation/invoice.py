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
username=input("enter your mail id or mobile number")
password=input("enter your password")
time.sleep(3)
usernamebox=driver.find_element_by_xpath('//*[@id="ap_email"]')
usernamebox.send_keys(username)
username_continue=driver.find_element_by_xpath('//*[@id="continue"]')
username_continue.click()
time.sleep(1)

password_box=driver.find_element_by_xpath('//*[@id="ap_password"]')
password_box.send_keys(password)
password_click=driver.find_element_by_xpath('//*[@id="signInSubmit"]')
password_click.click()
