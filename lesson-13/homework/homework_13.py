import numpy as np
matrix_13 = np.random.rand(3, 3)
vector_13 = np.random.rand(3, 1)  # Column vector
product_13 = np.dot(matrix_13, vector_13)
print("\n13. 3x3 Random Matrix:\n", matrix_13)
print("3x1 Column Vector:\n", vector_13)
print("Matrix-Vector Product (3x1):\n", product_13)