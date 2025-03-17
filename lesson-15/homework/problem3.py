import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-5, 5, 100)  # For x^3 and sin(x)
x2 = np.linspace(-5, 5, 100)  # For e^x
x3 = np.linspace(0, 5, 100)   # For log(x+1), x >= 0

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x1, x1**3, 'r')
plt.title('$f(x) = x^3$')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(2, 2, 2)
plt.plot(x1, np.sin(x1), 'g')
plt.title('$f(x) = \sin(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(2, 2, 3)
plt.plot(x2, np.exp(x2), 'b')
plt.title('$f(x) = e^x$')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(2, 2, 4)
plt.plot(x3, np.log(x3 + 1), 'm')
plt.title('$f(x) = \log(x+1)$')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.tight_layout()
plt.show()