# This script recommends a random movie from The Movie Database (TMDb) API based on a user-selected genre.

# Import required libraries for HTTP requests, randomization, and environment variable handling
import requests
import random
from os import getenv
from dotenv import load_dotenv

# Load environment variables from a .env file for secure API key/token management
load_dotenv()

# Retrieve API key and token from environment variables
api_key = getenv("API_KEY")  # Note: This is defined but not used in the current code
api_token = getenv("API_TOKEN")

# Define the TMDb API endpoint for discovering movies
url = "https://api.themoviedb.org/3/discover/movie"

# Dictionary mapping genre names to their TMDb genre IDs
genres = {
    'action': 28,
    'adventure': 12,
    'animation': 16,
    'comedy': 35,
    'crime': 80,
    'documentary': 99,
    'drama': 18,
    'family': 10751,
    'fantasy': 14,
    'history': 36,
    'horror': 27,
    'music': 10402,
    'mystery': 9648,
    'romance': 10749,
    'science fiction': 878,
    'tv movie': 10770,
    'thriller': 53,
    'war': 10752,
    'western': 37,
}

def get_movie():
    # Start an infinite loop to prompt the user for a genre until a valid input or 'quit' is received
    while True:
        i = 1
        # Display all available genres with numbered options
        for key in genres.keys():
            print(f"{i}. {key}")
            i += 1
        print("Type 'quit' to exit.")
        
        # Get user input for the desired movie genre and convert it to lowercase
        genre = input("Enter the genre of the movie: ").lower()
        # Exit the program if the user types 'quit'
        if genre == "quit":
            print("Goodbye!")
            return
        # Check if the entered genre is valid; if not, prompt again
        if genre not in genres:
            print("Invalid genre. Please try again.")
            continue
        # Get the TMDb genre ID corresponding to the selected genre
        genre_id = genres[genre]
        break  # Exit the loop once a valid genre is selected

    # Define parameters for the API request
    params = {
        # "api_key": api_key,  # Commented out; not used since Bearer token is used instead
        "with_genres": genre_id,  # Filter movies by the selected genre ID
        "language": "en-US",  # Specify response language as English (US)
    }
    # Define headers for the API request, including the Bearer token for authentication
    headers = {
        "accept": "application/json",  # Request JSON response format
        "Authorization": f"Bearer {api_token}"  # Use API token for authentication
    }

    try:
        # Send a GET request to the TMDb API with the specified parameters and headers
        response = requests.get(url, params=params, headers=headers)
        # Check if the response status indicates failure
        if not response.ok:
            print(f"Error: API request failed with status code {response.status_code}")
            return
        
        # Parse the JSON response into a Python dictionary
        data = response.json()
        # Extract the list of movies from the 'results' key, defaulting to an empty list if missing
        movies = data.get("results", [])
        # Check if any movies were returned for the selected genre
        if not movies:
            print(f"No movies found for the genre '{genre}'.")
            return
        
        # Randomly select one movie from the list of results
        movie = random.choice(movies)
        # Extract movie details, providing fallbacks for missing data
        title = movie["title"]
        release_date = movie.get("release_date", "Unknown Date")  # Note: Extra space in key might be a typo
        overview = movie.get("overview", "No description available.")
        
        # Print the recommended movie details in a formatted manner
        print("\nRecommended Movie:\n")
        print(f"Title: {title}")
        print(f"Release Date: {release_date}")
        print(f"Overview: {overview}")
        
    # Handle network or request-related errors
    except requests.RequestException as e:
        print(f"Error during API request: {e}")
    # Handle JSON parsing errors
    except ValueError as e:
        print(f"Error parsing response: {e}")

# Check if the script is run directly and call the main function
if __name__ == "__main__":
    get_movie()