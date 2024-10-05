import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel('axis x')
plt.ylabel('axis y')
plt.title('Graph of the function y=x**2')
plt.grid(True)
plt.show()