from bs4 import BeautifulSoup

# Open and read the HTML file with UTF-8 encoding
with open('weather.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table body and all rows
tbody = soup.find('tbody')
rows = tbody.find_all('tr')

# Create a list to store weather data
weather_data = []
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()              # Get the day
    temp_raw = cols[1].text.strip()         # Get the temperature as text
    temp = float(temp_raw.replace('°C', '')) # Convert temperature to float
    condition = cols[2].text.strip()        # Get the weather condition
    weather_data.append({'day': day, 'temp': temp, 'condition': condition})

# Print the 5-day forecast
print("5-Day Weather Forecast:")
print("-" * 30)
for data in weather_data:
    print(f"Day: {data['day']:<10} Temperature: {data['temp']}°C  Condition: {data['condition']}")

# Find the day with the highest temperature
max_temp_day = max(weather_data, key=lambda x: x['temp'])
print("\nHighest Temperature:")
print(f"Day: {max_temp_day['day']} - {max_temp_day['temp']}°C")

# List all sunny days
sunny_days = [data['day'] for data in weather_data if data['condition'] == 'Sunny']
print("\nSunny Days:")
for day in sunny_days:
    print(day)

# Calculate and print the average temperature
avg_temp = sum(data['temp'] for data in weather_data) / len(weather_data)
print(f"\nAverage Temperature: {avg_temp:.1f}°C")