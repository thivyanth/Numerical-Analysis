import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.laguerre import laggauss

def gauss_laguerre_integral_c(N):
    x, w = laggauss(N)
    integral = sum(w * np.sin(x))
    return integral

# Testing for different values of N
Ns = range(1, 50)
integral_values = [gauss_laguerre_integral_c(N) for N in Ns]

# Plotting the result
plt.plot(Ns, integral_values)
plt.xlabel('N')
plt.ylabel('Integral Value')
plt.title('Convergence of Gauss-Laguerre Quadrature for Integral (c)')
plt.show()
