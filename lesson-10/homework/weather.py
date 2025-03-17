# This script retrieves and displays current weather information for a given city using the OpenWeatherMap API.

# Import necessary libraries for making HTTP requests and handling environment variables
import requests
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('WEATHER_API')

# Define URLs for OpenWeatherMap APIs
url = 'https://api.openweathermap.org/data/2.5/weather'
location_url = 'http://api.openweathermap.org/geo/1.0/direct'

def get_weather(city_name):
    # Parameters for getting geographical coordinates from city name
    # Note: 'units' is not necessary for the geo API, but it's included here
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        # Make a GET request to get the list of locations matching the city name
        response = requests.get(location_url, params=params)
        response.raise_for_status()
        response_data = response.json()
        if not response_data:
            print("Error: Could not find the city.")
            return
        # Get the last location from the list (note: this might not be the most relevant one)
        longitude = response_data[-1]['lon']
        latitude = response_data[-1]['lat']
        print(f"Longitude of {city_name}: {longitude}")
        print(f"Latitude of {city_name}: {latitude}")
        
        # Parameters for getting weather data using the obtained coordinates
        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': api_key,
            'units': 'metric'  # Use metric units for temperature, humidity, etc.
        }
        # Make a GET request to get the current weather data
        response = requests.get(url, params=params)
        weather_data = response.json()
        main = weather_data['main']
        weather = weather_data['weather'][0]
        
        # Print weather information
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Description: {weather['description']}")
    
    except requests.RequestException as e:
        print(f"Error during API request: {e}")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)