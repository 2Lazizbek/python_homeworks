import numpy as np
matrix_7 = np.random.rand(5, 5)
normalized_matrix = (matrix_7 - np.min(matrix_7)) / (np.max(matrix_7) - np.min(matrix_7))
print("\n7. Original 5x5 Random Matrix:\n", matrix_7)
print("Normalized 5x5 Matrix:\n", normalized_matrix)