import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

URL = "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.find_all('div', class_='card')
    jobs = []
    
    # Extract job details from each card
    for card in job_cards:
        title = card.find('h2', class_='title').text.strip()
        company = card.find('h3', class_='company').text.strip()
        location = card.find('p', class_='location').text.strip()
        apply_link_tag = card.find_all('a', class_='card-footer-item')[1]
        apply_link = apply_link_tag['href']
        
        # Fetch job description from the apply link
        desc_response = requests.get(apply_link)
        desc_soup = BeautifulSoup(desc_response.text, 'html.parser')
        description = desc_soup.find('div', class_='content').find('p').text.strip()
        
        jobs.append((title, company, location, description, apply_link))
    
    return jobs

def create_database():
    # Create SQLite database and jobs table
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            JobTitle TEXT,
            CompanyName TEXT,
            Location TEXT,
            Description TEXT,
            ApplicationLink TEXT,
            PRIMARY KEY (JobTitle, CompanyName, Location)
        )
    ''')
    conn.commit()
    conn.close()

def load_existing_jobs():
    # Load existing jobs from the database
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT JobTitle, CompanyName, Location, Description, ApplicationLink FROM jobs")
    existing_jobs = cursor.fetchall()
    conn.close()
    print({(job[0], job[1], job[2]): (job[3], job[4]) for job in existing_jobs})
    return {(job[0], job[1], job[2]): (job[3], job[4]) for job in existing_jobs}

def update_database(jobs):
    # Update database with new or updated jobs
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    existing_jobs = load_existing_jobs()
    new_count = 0
    updated_count = 0
    
    for job in jobs:
        title, company, location, description, link = job
        key = (title, company, location)
        
        # Insert new job or update existing one
        if key not in existing_jobs:
            cursor.execute('''
                INSERT INTO jobs (JobTitle, CompanyName, Location, Description, ApplicationLink)
                VALUES (?, ?, ?, ?, ?)
            ''', job)
            new_count += 1
        elif (description, link) != existing_jobs[key]:
            cursor.execute('''
                UPDATE jobs
                SET Description = ?, ApplicationLink = ?
                WHERE JobTitle = ? AND CompanyName = ? AND Location = ?
            ''', (description, link, title, company, location))
            updated_count += 1
    
    conn.commit()
    conn.close()
    print(f"Added {new_count} new jobs, updated {updated_count} existing jobs.")

def filter_jobs(filter_type, filter_value):
    # Filter jobs by location or company
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    
    if filter_type.lower() == 'location':
        cursor.execute("SELECT * FROM jobs WHERE Location = ?", (filter_value,))
    elif filter_type.lower() == 'company':
        cursor.execute("SELECT * FROM jobs WHERE CompanyName = ?", (filter_value,))
    else:
        print("Invalid filter type. Use 'location' or 'company'.")
        conn.close()
        return []
    
    filtered_jobs = cursor.fetchall()
    conn.close()
    return filtered_jobs

def export_to_csv(filtered_jobs, filename='filtered_jobs.csv'):
    # Export filtered jobs to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['JobTitle', 'CompanyName', 'Location', 'Description', 'ApplicationLink'])
        writer.writerows(filtered_jobs)
    print(f"Exported {len(filtered_jobs)} jobs to {filename}")

if __name__ == "__main__":
    # Main workflow: scrape, update, filter, and export jobs
    create_database()
    scraped_jobs = scrape_jobs()
    update_database(scraped_jobs)
    
    print("\nFilter job listings:")
    filter_type = input("Enter filter type (location/company): ").lower()
    filter_value = input(f"Enter {filter_type} to filter by (e.g., 'Stewartbury, AA' or 'Payne, Roberts and Davis'): ")
    
    filtered_jobs = filter_jobs(filter_type, filter_value)
    if filtered_jobs:
        filename = f"{filter_type}_{filter_value.replace(', ', '_').replace(' ', '_')}_jobs.csv"
        export_to_csv(filtered_jobs, filename)
    else:
        print("No jobs found matching your filter criteria.")