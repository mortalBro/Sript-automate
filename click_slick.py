# from lib2to3.pgen2 import driver
# from selenium import webdriver

# driver_path = "PATH:/usr/local/bin/chromedriver"
# browser = webdriver.Chrome(executable_path=driver_path)

# # page_link="https://admin.myfavoriteartistheadphones.net/album/create"
# page_link="https://www.onlinegdb.com/login?next=https://www.onlinegdb.com/myfiles"
# browser.get(page_link)
# #/html/body/div[1]/div/div/div/div[1]/div[2]/ul/li[5]/a
# # x_path="/html/body/div[1]/div/div/div/div[3]/div/div/div[3]/div/div/div/div/div/div/form/div[1]/input"

# #https://www.onlinegdb.com/myfiles


# # name_field = browser.find_element_by_xpath(x_path)

# # name_field.send_keys('John Doe')


# # Find the button by its CSS selector or XPath expression
# button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/ul/li[5]/a")

# button.click()

# # Close the browser
# browser.quit()


from selenium import webdriver

# Set up the web driver
driver = webdriver.Chrome()
# "PATH:/usr/local/bin/chromedriver"
# Navigate to the webpage with the form
driver.get('https://www.onlinegdb.com/login')

# Find the name field element using XPath
email = driver.find_element("//*[@id='email']")

# Fill in the name field
email.send_keys('John Doe')

password = driver.find_element("//*[@id='password']")

# Fill in the name field
password.send_keys('John Doe')
# Submit the form
submit_button = driver.find_element("//*[@id='login-submit']")
submit_button.click()

# Close the browser
driver.quit()
