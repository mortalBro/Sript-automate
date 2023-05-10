from selenium import webdriver
from selenium.webdriver.common.by import By
import os
os.environ['PATH']+="PATH:/usr/local/bin/SeleniumDrivers"
#driver_path = "PATH:/usr/local/bin/chromedriver"
driver =webdriver.Chrome()

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_default")

element = driver.find_element(By.c,"download-counter btn btn-primary")
element.click()
i=0
while(True):
    i+=1
    if(i==1000):
        break
    pass