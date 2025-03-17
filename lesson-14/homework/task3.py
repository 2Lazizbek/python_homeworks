import numpy as np

# Define the coefficient matrix
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

# Define the right-hand side vector
b = np.array([7, 4, 5])

# Solve the system
solution = np.linalg.solve(A, b)

# Extract the values of x, y, and z
x, y, z = solution

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")