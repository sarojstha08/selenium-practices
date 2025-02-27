from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re #for regular expression
import random
import string
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#set url
url="https://www.mindrisers.com.np/contact-us"
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)

#finding input places
Name_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
Email_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
subject_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
queries_field=driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))

#validate email
def Validate_Email(email):
    try:
        email_pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.search(email_pattern, email):
            return True
        else:
            return False
    except Exception as e:
        print(f"Validation error: {e}")
        return False
#sending random values as input 
#email
def generate_random_email():
    domain="automate.com"
    email_length=5
    random_string=''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email=random_string+"@"+domain
    return email
#name
def random_name():
    return ''.join(random.choices(string.ascii_letters, k=8))
#phone number
def random_number():
    return "+977-98" + ''.join(random.choices(string.digits, k=8))


#subject
def random_subject():
    return ''.join(random.choices(string.ascii_letters, k=8))

#queries
def random_queries():
    return ''.join(random.choices(string.ascii_letters, k=20))

#generate values
email=generate_random_email()
name=random_name()
number=random_number()
subject=random_subject()
queries=random_queries()
#check if empty
if not name:
    print("this field cannot be empty")

#imput values to the field
Name_field.clear()
Name_field.send_keys(name)
time.sleep(3)

#email validation
if Validate_Email(email):
    print("valid email")
else:
    print("invalid email")

Email_field.clear()
Email_field.send_keys(email)
time.sleep(2)

phone_field.clear()
phone_field.send_keys(number)
time.sleep(2)

subject_field.clear()
subject_field.send_keys(subject)
time.sleep(2)

queries_field.clear()
queries_field.send_keys(queries)
time.sleep(2)


#quit window after a while
time.sleep(3)
driver.quit()