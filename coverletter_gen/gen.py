import cohere
import os
from dotenv import load_dotenv

load_dotenv()
# from linkedin_scraping.jobscrape import job_scrape

cohere_api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(cohere_api_key)

def generate_cover_letter(keywords):
    # Build a prompt with the keywords to generate a custom cover letter
    prompt = f"Write a professional cover letter for a job application. Include these keywords: {keywords}. Keep it concise and focused."

    # Generate text using Cohere's model
    response = co.generate(
        model='command-xlarge-nightly',  # Or any other model variant available
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )

    # Extract generated cover letter text
    cover_letter = response.generations[0].text.strip()
    return cover_letter


def save_to_file(content, count):
    filename = f"cover_letter_{count}.txt"
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Cover letter saved as {filename}")
    




