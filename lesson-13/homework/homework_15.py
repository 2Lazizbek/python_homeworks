import numpy as np
matrix_15 = np.random.rand(5, 5)
row_sums = np.sum(matrix_15, axis=1)  # Sum across columns (row-wise)
col_sums = np.sum(matrix_15, axis=0)  # Sum across rows (column-wise)
print("\n15. 5x5 Matrix:\n", matrix_15)
print("Row-wise sums:", row_sums)
print("Column-wise sums:", col_sums)