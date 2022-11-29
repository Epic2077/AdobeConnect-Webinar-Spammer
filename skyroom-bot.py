from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import random
import platform
import os

x = platform.system()
if x == "Windows" :
	os.system('cls')

LENAME = ""
URL = input('Paste the URL: ') # Put your URL here
IFTEXT = input('Enable Textspam Y/N: ')
if IFTEXT == "Y" or IFTEXT == "y":
	texttospam = input('Text to spam: ') # The text to spam goes here
IFHAND = input('Enable Handspam Y/N: ')
CUSTOMNAME = input("Enable Custom Name Y/N (Don't enable with namespam cus it's pointless): ")
if CUSTOMNAME == "Y" or CUSTOMNAME == "y":
	LENAME = input('Type your name: ')
IFNAME = input('Enable Namespam Y/N: ')
print('')
print('Trying to launch Firefox...')
time.sleep(10)
print('Firefox Launched.')
print('Please Wait...')
print('')


profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")
driver = webdriver.Firefox(firefox_profile=profile)
driver.get(URL)
wait = WebDriverWait(driver, 600)

# LOGIN
time.sleep(1)
cum = driver.find_element_by_xpath('//*[@id="btn_guest"]')
cum.click()
time.sleep(5)
cum1 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/input')
cum1.send_keys('yes') # Your Name
time.sleep(1)
cum2 = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[2]/button')
cum2.click()
time.sleep(1)

# le script
if LENAME != "":
	driver.execute_script("window.localStorage.setItem('nickname',"+"'"+'"'+LENAME+'"'+"'"");")
	time.sleep(1)
	driver.refresh()
	time.sleep(1)
	cum = driver.find_element_by_xpath('//*[@id="btn_guest"]')
	cum.click()
	time.sleep(3)

cum3 = driver.find_element_by_xpath('//*[@id="app_menu"]/div/button')
cum3.click()
time.sleep(1)
cum4 = driver.find_element_by_xpath('/html/body/nav[1]/ul/li[1]')
cum4.click()
time.sleep(1)

def changename():
	if IFNAME == "Y" or IFNAME == "y":
		try:
			print('Executing Name Spam')
			name = ['gay','balls','sex','dababy','less gooo','cum'] # List of names to change
			name2 = random.choice(name)
			cum3 = driver.find_element_by_xpath('//*[@id="app_menu"]/div/button')
			cum3.click()
			cum4 = driver.find_element_by_xpath('/html/body/nav[1]/ul/li[1]')
			cum4.click()
			cum5 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td/div/div[1]/button')
			cum5.click()
			cum6 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td/div/div[2]/form/input')
			cum6.clear()
			print (name2)
			cum6.send_keys(name2)
			time.sleep(0.2)
			cum7 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/table/tbody/tr[3]/td/div/div[2]/form/button')
			cum7.click()
		except:
			print('1')

def textspam():
	if IFTEXT == "Y" or IFTEXT == "y":
		print('Executing Text Spam')
		#name = ['gay','balls','sex','dababy','less gooo','cum'] NOT USED
		name2 = texttospam
		cum8 = driver.find_element_by_xpath('//*[@id="sidebar"]/div[4]/div[2]/div/div[2]/div[3]/div[1]')
		cum8.send_keys(texttospam)
		cum8.send_keys(Keys.RETURN)

def handspam():
	if IFHAND == "Y" or IFHAND == "y":
		print('Executing Hand Spam')
		cum9 = driver.find_element_by_xpath('//*[@id="toolbar"]/button[7]')
		cum9.click()

# If you want to disable anything just delete it from here
while 1 == 1:
	textspam()
	changename()
	textspam()
	handspam()
	textspam()
