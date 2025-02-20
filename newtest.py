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


time.sleep(3)
driver.quit()