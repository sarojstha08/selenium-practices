from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set path to Brave browser
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Adjust if necessary

# Set up Brave options
options = Options()
options.binary_location = brave_path  # Specify the Brave binary location

# Set path to ChromeDriver
chromedriver_path = "C:/path/to/chromedriver.exe"  # Adjust to your actual chromedriver path
service = Service(chromedriver_path)

# Initialize WebDriver with Brave
driver = webdriver.Chrome(service=service, options=options)

# Open a website
driver.get("https://www.google.com")

# Close the browser after use
driver.quit()
