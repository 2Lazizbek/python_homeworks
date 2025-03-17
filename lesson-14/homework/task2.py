import numpy as np

# Define the power function
def raise_to_power(base, exponent):
    return base ** exponent

# Vectorize the function
vectorized_power = np.vectorize(raise_to_power)

# Define the input arrays
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

# Calculate the results
result = vectorized_power(bases, exponents)

# Print results
print("Bases:", bases)
print("Exponents:", exponents)
print("Results:", result)