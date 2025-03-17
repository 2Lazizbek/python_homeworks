import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c='blue', marker='o', label='Random Points', alpha=0.6)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of 100 Random Points')
plt.grid(True)
plt.legend()
plt.show()