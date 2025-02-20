
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


Name = driver.find_element(By.XPATH,("//input[@id='full_name']"))
Email= driver.find_element(By.XPATH,("//input[@id='email']"))
Phone = driver.find_element(By.XPATH,("//input[@id='mobile_no']"))

College_Name= driver.find_element(By.XPATH,("//input[@id='college']")) 

Academic_status = driver.find_element(By.ID, ("qualification")) 
dropdown =Select(Academic_status)
# Academic_Dropdown = driver.find_element(By.XPATH("/html/body/div[1]/div[1]/section/form/div[1]/div[1]"))
Interested_course= driver.find_element(By.ID,("course")) 
course=Select(Interested_course)

Preferred_schedule= driver.find_element(By.ID,("shedule")) 
shedule=Select(Preferred_schedule)
# Internship= driver.find_element(By.XPATH,("//input[@id='remarks-yes']")) 
Queries= driver.find_element(By.XPATH,("//textarea[@id='question']")) 





Name.send_keys("Saroj")
time.sleep(2)
Email.send_keys("sarojstha7887@gmail.com")
time.sleep(2)
Phone.send_keys("9823119243")
time.sleep(2)
College_Name.send_keys("Nepalaya College")
time.sleep(2)
dropdown.select_by_index(2)
time.sleep(2)
course.select_by_index(3)
time.sleep(2)
shedule.select_by_index(2)
time.sleep(2)
# Interested_course.select_by_visible_text("Quality Assurance Training in Nepal")
# time.sleep(2)
# Preferred_schedule.select_by_visible_text("Evening")
# time.sleep(2)
# Internship.click()
# time.sleep(2)
Queries.send_keys("If you have any queries then please visit our main branch at putalisadak,, opposite to edwise academy!!")
time.sleep(2)

#scrolling the page

driver.execute_script("window.scrollBy(0,500)")
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
