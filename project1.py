from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert


import time
#set up a driver installation
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


# Set Edge options to disable notifications
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--disable-notifications")

# Set up WebDriver with Edge options
driver = webdriver.Edge(options=edge_options)

edge_options.add_argument("--headless")


#provide a website
url = "https://merolagani.com/"


driver.get(url)
driver.maximize_window()
time.sleep(2)

market = driver.find_element(By.XPATH,("//a[normalize-space()='Market']"))
market.click()
time.sleep(2)
try:
    alert = Alert(driver)
    alert.dismiss()  # Dismiss the pop-up
except:
    print("No alert found")

live_trading = driver.find_element(By.XPATH,("//a[normalize-space()='Live Trading']"))
live_trading.click()
time.sleep(2)

aclbsl= driver.find_element(By.XPATH,("//a[normalize-space()='ACLBSL']"))
aclbsl.click()
time.sleep(2)

#new tab opened so need to switch the mouse to the new tab 
driver.switch_to.window(driver.window_handles[1])  # Move to the new tab
time.sleep(2)

# Scrolling the Page
driver.execute_script("window.scrollBy(0,800)")
time.sleep(2)

price_history= driver.find_element(*(By.XPATH,"//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab']"))
price_history.click()
time.sleep(2)

date = driver.find_element(*(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter']"))
date.send_keys("12/02/2025")
time.sleep(3)


time.sleep(3)
driver.quit()