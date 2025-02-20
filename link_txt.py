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
url = "https://meroshare.cdsc.com.np/#/login"

driver.get(url)
driver.maximize_window()
time.sleep(2)




Depositery = driver.find_element(*(By.XPATH,"/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]"))
dropdown=Select(Depositery)

username = driver.find_element(By.ID,"username")



dropdown.select_by_index("2")
username.send_keys("Sarojstha")

time.sleep(2)
driver.quit()