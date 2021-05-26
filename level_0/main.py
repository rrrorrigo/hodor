#!/usr/bin/python3
""" Program that votes 1024 times for id (2757 in my case)"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://158.69.76.135/level0.php")
for i in range(1024):
        username = driver.find_element_by_xpath("//input[@name='id']")
        button = driver.find_element_by_name('holdthedoor')
        username.send_keys("2757")
        button.click()
        driver.implicitly_wait(5)
driver.quit()
