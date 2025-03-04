from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


ACCOUNT_EMAIL="shivankarjay@gmail.com"
ACCOUNT_PASSWORD="jay@135790"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to linkedin
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4156901053&geoId=114806696&keywords=android%20developer%20jobs&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
time.sleep(2)
sign_in_button  = driver.find_element(by=By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]')
sign_in_button.click()

time.sleep(2)
email=driver.find_element(by=By.XPATH,value='//*[@id="base-sign-in-modal_session_key"]')
email.send_keys("shivankarjay@gmail.com")
password=driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal_session_password"]')
password.send_keys("jay@135790")

time.sleep(2)
sign_in_2 = driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
sign_in_2.click()