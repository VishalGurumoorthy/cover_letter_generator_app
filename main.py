from linkedin_scraping.login import linkedin_login
from linkedin_scraping.jobscrape import job_scrape
from coverletter_gen.gen import generate_cover_letter, save_to_file
from coverletter_gen.send_mail import send_email_with_attachments
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os

load_dotenv()


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run hadless Chrome
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

if __name__ == "__main__":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    linkedin_login(driver)
    time.sleep(1)
    job_listings = job_scrape(driver)
    time.sleep(2)
    
    keywords = ""
    count = 0
    for listing in job_listings:
        count+=1
        if(len(listing)>0):
            lines = listing.split("\n")
            role = lines[0]  # Assuming the role name is in the first line
            company = lines[2]  # Assuming the company name is in the third line
            keywords+=(f"{role}, {company}")
            result = generate_cover_letter(keywords)
            save_to_file(result, count)
            time.sleep(2)
    
    file_names = ["cover_letter_1.txt", "cover_letter_2.txt", "cover_letter_3.txt"]
    attachment_paths = ["./{}".format(file_name) for file_name in file_names]  # Assumes files are in the current directory

    send_email_with_attachments(
        sender_email= os.getenv("sender_email"),
        sender_password=os.getenv("app_password"),
        recipient_email=os.getenv("reciever_email"),
        subject="Custom Email with Attachments",
        body=f"Promoted job cover letters generated are attached for + {keywords}",
        attachment_paths=attachment_paths
    )

            
    
    
    
    