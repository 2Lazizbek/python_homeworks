from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time

# Function to scrape laptop data from Demoblaze using Selenium
def scrape_laptops():
    # Initialize the Chrome WebDriver (ensure chromedriver is installed and in PATH)
    driver = webdriver.Chrome()
    
    # Base URL for the Demoblaze homepage
    url = "https://www.demoblaze.com/index.html"
    laptop_data = []

    # Navigate to the homepage
    driver.get(url)

    # Click on the "Laptops" category link (adjust XPath based on actual site structure)
    driver.find_element(By.XPATH, "//a[contains(text(), 'Laptops')]").click()
    
    # Wait for the laptops section to load
    time.sleep(3)

    # Scrape data across multiple pages (assuming 2 pages for this example)
    for page in range(1, 3):
        # Parse the current page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all laptop cards (adjust class based on actual site structure)
        laptops = soup.find_all('div', class_='card')
        
        # Loop through each laptop card to extract details
        for laptop in laptops:
            # Extract laptop name from the card title
            name = laptop.find('h4', class_='card-title').text.strip()
            # Extract price (assuming it's in an h5 tag)
            price = laptop.find('h5').text.strip()
            # Extract description (assuming it's in a p tag)
            description = laptop.find('p').text.strip()

            # Append the extracted data to the list as a dictionary
            laptop_data.append({
                "name": name,
                "price": price,
                "description": description
            })

        # Click the "Next" button if it exists (adjust ID or XPath as needed)
        try:
            next_button = driver.find_element(By.ID, "next2")
            next_button.click()
            # Wait for the next page to load
            time.sleep(3)
        except:
            # Break the loop if no "Next" button is found (end of pages)
            break

    # Close the browser
    driver.quit()

    # Save the collected data to a JSON file
    with open('laptops.json', 'w') as f:
        json.dump(laptop_data, f, indent=2)

    # Return the data for further use if needed
    return laptop_data

# Execute the scraping function and print the result
data = scrape_laptops()
print(json.dumps(data, indent=2))