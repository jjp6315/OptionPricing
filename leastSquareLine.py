import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

ln_N = np.array([10, 100, 1000, 10000])
ln_E = np.array([0.01226312622, 0.00124186009, 0.00012403297, 0.00001210981])

slope, intercept, r_value, p_value, std_err = linregress(np.log(ln_N), np.log(ln_E))

A = slope
B = intercept

plt.scatter(np.log(ln_N), np.log(ln_E), label='Data')

x = np.linspace(min(np.log(ln_N)), max(np.log(ln_N)))
plt.plot(x, A*x + B, color='red', label='Least Squares Line')

plt.xlabel('ln N')
plt.ylabel('ln |E|')
plt.title('ln |E| vs ln N')
plt.legend()
plt.grid(True)
plt.show()

print("A:", A)
print("B:", B)

