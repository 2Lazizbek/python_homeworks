import numpy as np

# Define the conversion function
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Vectorize the function
vectorized_convert = np.vectorize(fahrenheit_to_celsius)

# Array of temperatures in Fahrenheit
temp_array = np.array([32, 68, 100, 212, 77])

# Convert the array
result = vectorized_convert(temp_array)

# Print results
print("Fahrenheit temperatures:", temp_array)
print("Celsius temperatures:", result.round(2))