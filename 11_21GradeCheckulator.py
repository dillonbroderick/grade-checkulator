from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ctypes
from twilio.rest import Client

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

i = 0
EXPECTED_GRADE = "95.6"
USER = "REDACTED"
PASS = "REDACTED"

def loginAndCheckGrade():
    driver.get("https://powerschool.sandi.net/public/")

    time.sleep(5)

    try:
        user1 = driver.find_element_by_id("fieldAccount")
        user1.send_keys(USER)

        pass1 = driver.find_element_by_id("fieldPassword")
        pass1.send_keys(PASS)
        pass1.send_keys(Keys.RETURN)
        
    except:
        #do Nothing
        print("Do Nothing")
        
    time.sleep(5)

    frerichsGrade = driver.find_element_by_css_selector("#ccid_34518696 > td:nth-child(15) > a")
    s = frerichsGrade.text
    a = s[1:6]
    
    if EXPECTED_GRADE in a:
        print("Iteration done")
        time.sleep(1790)
    else:
        i = 2

while i < 1:
    loginAndCheckGrade()

client = Client("REDACTED", "REDACTED")
client.messages.create(to="+1REDACTED", from_="+1REDACTED", body="Update Detected")


        
