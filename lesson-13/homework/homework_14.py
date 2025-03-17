import numpy as np
matrix_14a = np.random.rand(3, 3)
vector_14b = np.random.rand(3, 1)  # Column vector
solution_14 = np.linalg.solve(matrix_14a, vector_14b)
print("\n14. 3x3 Matrix A:\n", matrix_14a)
print("3x1 Vector b:\n", vector_14b)
print("Solution x (3x1):\n", solution_14)