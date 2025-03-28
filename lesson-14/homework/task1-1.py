import numpy as np

@np.vectorize
def to_celcius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

temperatures = np.array([32, 68, 100, 212, 77])
print("Fahrenheit temperatures:", temperatures.tolist())
print(temperatures)
print("Celsius temperatures:", to_celcius(temperatures).tolist())