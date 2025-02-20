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
url = "https://filebin.net"


driver.get(url)
driver.maximize_window()
time.sleep(2)

upload_files= driver.find_element(By.XPATH, ("//input[@id='fileField']"))
upload_files.send_keys("C:/Users/user/OneDrive/Pictures/Camera Roll/WIN_20230424_11_40_05_Pro.jpg")
time.sleep(2)

more = driver.find_element(By.XPATH, ("//a[@id='dropdownFileMenuButton']"))
more.click()
time.sleep(2)


time.sleep(5)
driver.quit()
