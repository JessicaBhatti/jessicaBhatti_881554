# Open the web browser(chrome)
# Open URL  "https://www.pinterest.ca/"
# Click on login button to navigate to the username and password
# Enter username "jessica.bhatti.2604@gmail.com"
# Enter password " Jess@1234"
# CLick on login
# Close Browser


# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.pinterest.ca/")
time.sleep(8)

driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div["
                            "2]/button/div/div").click()
time.sleep(4)
username = driver.find_element("id", "email")
username.clear()
username.send_keys("jessica.bhatti.2604@gmail.com")

password = driver.find_element("id", "password")
password.clear()
password.send_keys("Jess@1234")
time.sleep(10)

driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/form/div[7]/button").click()
time.sleep(15)
driver.close()
