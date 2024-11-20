from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())


def job_scrape(driver):   

    driver.get('https://www.linkedin.com/jobs/')
    time.sleep(5)

    # Scrape job listings
    jobs = driver.find_elements(By.ID,"jobs-home-vertical-list__entity-list")
    job_list = []
    
    job = jobs[0].text

    job_listings = re.findall(r'(.*)', job, re.DOTALL)

    
    for job in job_listings:
        val = job.strip()
        job_list.append(val)
        
    job_list = job_list[0]
    
    print(job_list)
    job_list = re.split(r"Viewed|ago", job_list)
        

    
        # val = list(val)
    time.sleep(1)
    print(job_list)
    # Close the browser
    return job_list