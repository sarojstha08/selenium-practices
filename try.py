# # Import Necessary Driver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time

# #set up a driver installation
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# #provide a website
# url = "https://formy-project.herokuapp.com/form"

# driver.get(url)
# driver.maximize_window()
# time.sleep(2)


# firstname = driver.find_element(By.XPATH,("//input[@id='first-name']"))
# lastname = driver.find_element(By.XPATH,("//input[@id='last-name']"))
# jobtitle = driver.find_element(By.XPATH,("//input[@id='job-title']"))
# education_level = driver.find_element(By.XPATH,("//input[@id='radio-button-3']"))
# gender = driver.find_element(*())

# firstname.send_keys("John")
# time.sleep(2)
# lastname.send_keys("Doe")
# time.sleep(2)
# jobtitle.send_keys("QA Engineer")
# time.sleep(2)
# education_level.click
# time.sleep(2)


# title = driver.current_url


# time.sleep(5)

# driver.quit()


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
url = "https://www.mindrisers.com.np/online-admission"


driver.get(url)
driver.maximize_window()
time.sleep(2)

driver.execute_script("window.scrollBy(0,800)")
time.sleep(2)


academic_status=driver.find_element(By.ID,"qualification")
dropdown=Select(academic_status)

dropdown.select_by_index(2)
time.sleep(2)


driver.quit()
time.sleep(2)