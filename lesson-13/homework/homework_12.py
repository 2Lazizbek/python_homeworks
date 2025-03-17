import numpy as np
matrix_12a = np.random.rand(3, 4)
matrix_12b = np.random.rand(4, 3)
product_12 = np.dot(matrix_12a, matrix_12b)
print("\n12. 3x4 Matrix A:\n", matrix_12a)
print("4x3 Matrix B:\n", matrix_12b)
print("Matrix Product A · B (3x3):\n", product_12)