# pylint: disable=broad-except
# pylint: disable=invalid-name

import time
import random
import platform
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

text_to_spam, spam_hand, custom_name, name_spam = [None]*4

x = platform.system()
if x == "Windows":
    os.system('cls')


DEFAULT_NAME = "guest"


url = input("Enter the URL: ")
# ask to whether enable text spam or not
if_text_spam = input("Do you want to enable Text Spam? (y/N): ")
if if_text_spam in ("Y", "y"):
    text_to_spam = input('Text to spam: ') # The text to spam goes here
# ask to whether enable hand spam or not
if_hand_spam = input('Do you want to enable Hand Spam? (y/N): ')
if if_hand_spam in ("Y", "y"):
    spam_hand = True
# ask to whether enable custom name or not
if_custom_name = input("Do you want to enable Custom Name? (Don't enable with namespam cus it's pointless) (y/N): ")
if if_custom_name in ("Y", "y"):
    custom_name = input('Type your name: ')
# ask to whether enable name spam or not
if_name_spam = input('Do you want to enable Name Spam (y/N): ')
if if_name_spam in ("Y", "y"):
    name_spam = True


print('\nTrying to launch Firefox...')

# INIT
profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0") # mute window
driver = webdriver.Firefox(firefox_profile=profile, executable_path=GeckoDriverManager().install())
driver.get(url)
wait = WebDriverWait(driver, 600)
print('Firefox Launched.')
print('Please Wait...\n')

# LOGIN
# Login method has two different posibilities.
# If this one doesn't work. make it a comment.
time.sleep(5)
guest_name_input = driver.find_element(By.XPATH, '//*[@id="guestName"]')
guest_name_input.send_keys(DEFAULT_NAME) # Your name
time.sleep(1)
login_button = driver.find_element(By.XPATH, '//*[@id="login-guest"]')
login_button.click()
time.sleep(5)

# Starting from here
cum0 = driver.find_element_by_xpath('/html/body/center/div[1]/div[3]/div[7]/button')
cum0.click()
time.sleep(15)
# Ending here.

# Then take this part out from being a comment.

# Starting here
# remember_button = driver.find_element(By.XPATH, '//*[@id="coral-id-0"]')
# remember_button.click()
# open_in_browser_button = driver.find_element(By.XPATH, '/html/body/coral-dialog/div[2]/coral-dialog-content/div[1]/div[1]')
# open_in_browser_button.click()
# Ending here.
input("Wait to get accepted, press any key when you are in the class.") #press Enter in cmd
driver.switch_to.frame(driver.find_element(By.ID, "html-meeting-frame"))
def spam_name_change():
    if name_spam:
        try:
            print('Executing Name Spam')
            names = ['Cum', 'Booba', 'Send nudes', 'Shit', 'Fuck', 'Dababy'] # List of names to change
            name = random.choice(names)
            three_dots = driver.find_elements(By.XPATH, '//*[@id="MultiLevelMenuButton"]')[2]
            three_dots.click()
            edit_my_info = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/ul/li[3]')
            edit_my_info.click()
            name_input = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div[7]/div/div[2]/div/div/div[2]/div[2]/input')
            print(f"Changing name to {name}")
            name_input.clear()
            name_input.send_keys(name)
            time.sleep(0.2)
            save_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div[7]/div/div[2]/div/div/div[3]/button[2]')
            save_button.click()
        except Exception as e:
            print(e)

def spam_text():
    if text_to_spam:
        try:
            print('Executing Text Spam')
            # name = ['gay','balls','sex','dababy','less gooo','cum'] NOT USED
            chat_input = driver.find_element(By.XPATH, '//*[@id="chatTypingArea"]')
            chat_input.send_keys(text_to_spam)
            chat_input.send_keys(Keys.RETURN)
        except Exception as e:
            print(e)

def spam_hand():
    if spam_hand:
        time.sleep(0.5)
        try:
            print('Executing Hand Spam')
            hand_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div[2]/div[2]/div[4]/div/button')
            hand_button.click()
        except Exception as e:
            print(e)

# If you want to disable anything just delete it from here
while True:
    spam_text()
    spam_name_change()
    spam_text()
    spam_hand()
    spam_text()

