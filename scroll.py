#Import Necessary Driver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#set up a driver installation
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


#provide a website
url = "https://www.mindrisers.com.np/"


driver.get(url)
driver.maximize_window()

#Calcuate Height of page
page_height = driver.execute_script("return document.body.scrollHeight")


scroll_speed = 300

scroll_iterations = int(page_height/scroll_speed)

#loop to perform scroll
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed})")
    time.sleep(2)

title = driver.title
print(title)
time.sleep(5)

driver.quit()

