from lib2to3.pgen2 import driver
import os
from selenium import webdriver
driver_path = "PATH:/usr/local/bin/chromedriver"
browser = webdriver.Chrome(executable_path=driver_path)
# page_link="https://admin.myfavoriteartistheadphones.net/album/create"
page_link="https://www.onlinegdb.com/login?next=https://www.onlinegdb.com/myfiles"
browser.get(page_link)

x_path="/html/body/div[1]/div/div/div/div[3]/div/div/div[3]/div/div/div/div/div/div/form/div[1]/input"

name_field = browser.find_element_by_xpath(x_path)
name_field.send_keys('John Doe')

button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/ul/li[5]/a")
button.click()

# Close the browser
# browser.quit()
