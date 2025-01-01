from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

#Login
def login():
    try:
    
        username = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input')
        username.click()
        username.send_keys("Enter username or Emai")
        time.sleep(3)
        password = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input')
        password.click()
        password.send_keys("Enter password")
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[3]').click()
        time.sleep(5)
    except NoSuchElementException:
        print("Login failed")
        login()
        

login()
    
driver.get("Enter the chat link")
time.sleep(3)

#notification pop up
try:
    driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()              
except Exception as e:
    print("Notification pop up not found")

time.sleep(5)


def deletion():

        #find the message
        try:
            msg = driver.find_element(By.CSS_SELECTOR, '.html-div.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1gslohp.x11i5rnm.x12nagc.x1mh8g0r.x1yc453h.x126k92a.xyk4ms5')
            msg.click()
            
            time.sleep(1)
        except Exception as e:  
            print("No message found")

            time.sleep(3)

        #more button
        try:
            morebtn = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="More"]')
            morebtn.click()
            
            time.sleep(1)
        except Exception as e:
            print("more button not found")

            time.sleep(3)

        #unsend button
        try:
            unsend = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[5]')
            unsend.click()
            time.sleep(1)
        except Exception as e:  
            print("Unsend button not found")

            time.sleep(3)

        #confirm unsend
        try:
            confirm = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/button[1]')
            confirm.click()
            time.sleep(1)
        except Exception as e:
            print("confrim unsend not found")

while True:
    deletion()
    time.sleep(1)
