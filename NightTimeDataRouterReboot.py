import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

## The following code is to restart a ZTE router to invoke and assure your night time data is going to be used when midnight strikes.This is for those of you using FIXED LTE deals with night time data.
## if you are using a different brand router

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.0.1/m/index.html#/login')

## This is where you can save your admin login password or username( note this is not totally safe but its okay if you are okay with it)

username = 'admin'
time.sleep(10)

routerLogin = driver.find_element_by_xpath('//*[@id="password"]')
routerLogin.send_keys('admin')
time.sleep(10)
clickLogin = driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
time.sleep(4)

advanceSet = driver.find_element_by_xpath('//*[@id="home_container"]/ul/li[5]/a')
advanceSet.send_keys(Keys.ENTER)

time.sleep(4)

restartDevice = driver.find_element_by_xpath('//*[@id="othersList"]/li[3]').click()
##restartDevice.send_keys(Keys.ENTER)

time.sleep(4)

restartBut = driver.find_element_by_xpath('//*[@id="yesbtn"]').click()


exit()