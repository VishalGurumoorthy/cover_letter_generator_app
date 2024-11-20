from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

load_dotenv()

def linkedin_login(driver):
    try:
        driver.get("https://www.linkedin.com/login")

        time.sleep(2)

        # Find the username and password fields
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")

        # Enter your LinkedIn credentials
        username_field.send_keys(os.getenv("YOUR_LINKEDIN_EMAIL"))
        password_field.send_keys(os.getenv("YOUR_LINKEDIN_PASSWORD"))

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Allow some time for the login process to complete
        time.sleep(5)

    # Check if login was successful by looking for the profile icon
    
        
        print("Login successful")
    except:
        print("Login failed")
