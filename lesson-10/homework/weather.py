import requests

API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        
        main = weather_data['main']
        weather = weather_data['weather'][0]
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Feels like: {main['feels_like']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Description: {weather['description']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Error: Could not parse weather data. Check if the city name is correct.")

get_weather("Tashkent")