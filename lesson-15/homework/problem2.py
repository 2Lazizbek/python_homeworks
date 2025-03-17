import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
sin_x = np.sin(x)
cos_x = np.cos(x)
plt.figure(figsize=(8, 6))
plt.plot(x, sin_x, 'r--o', label='$\sin(x)$', linewidth=2, markersize=5)  # Red dashed line with circles
plt.plot(x, cos_x, 'b-s', label='$\cos(x)$', linewidth=2, markersize=5)  # Blue solid line with squares
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid(True)
plt.show()