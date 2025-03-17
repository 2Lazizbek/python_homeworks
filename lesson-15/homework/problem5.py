import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, alpha=0.7, color='purple')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution (mean=0, std=1)')
plt.show()