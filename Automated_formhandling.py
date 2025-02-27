from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select

import time
#set up a driver installation
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

#provide a website
url = "https://formy-project.herokuapp.com/form"

driver.get(url)
driver.maximize_window()
time.sleep(2)


firstname = driver.find_element(By.XPATH,("//input[@id='first-name']"))
Lastname = driver.find_element(By.XPATH,("//input[@id='last-name']"))
job_title = driver.find_element(By.XPATH,("//input[@id='job-title']"))

education_level= driver.find_element(By.XPATH,("//input[@id='radio-button-1']")) 
Sex = driver.find_element(By.XPATH,("//input[@id='checkbox-1']")) 


# Initialize the Select class
dropdown_element = driver.find_element(By.ID, "select-menu")
dropdown = Select(dropdown_element)

date= driver.find_element(By.ID,"datepicker")


firstname.send_keys("roman")
time.sleep(2)
Lastname.send_keys("reigns")
time.sleep(2)
job_title.send_keys("QA Tester")
time.sleep(2)
education_level.send_keys("High School")
time.sleep(2)
Sex.send_keys("Male")
time.sleep(2)

driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)
# Select "0-1" option by visible text
dropdown.select_by_visible_text("0-1")
time.sleep(2)
date.send_keys("02/17/2025")

#scrolling the page

driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)

# username.send_keys("standard_user")
# time.sleep(2)

# password.send_keys("secret_sauce")
# time.sleep(2)

# login_button.click()

# title = driver.current_url

# if (title== "https://www.saucedemo.com/inventory.html"):
#     print("Login Successful")
# else:
#     print("Login Unsuccessful")
 
time.sleep(3)
driver.quit()
