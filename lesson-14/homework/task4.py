import numpy as np

# Define the coefficient matrix
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

# Define the right-hand side vector
b = np.array([12, -5, 15])

# Solve the system
solution = np.linalg.solve(A, b)

# Extract the values of I1, I2, and I3
I1, I2, I3 = solution

print(f"I1 = {I1}")
print(f"I2 = {I2}")
print(f"I3 = {I3}")