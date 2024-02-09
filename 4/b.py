import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

def transform_b(x):
    # Transform [0, pi/2] to [-1, 1]
    return (np.pi/4) * (x + 1)

def gauss_legendre_integral_b(N):
    x, w = leggauss(N)
    xt = transform_b(x)
    integral = sum(w * np.log(1 + xt)) * (np.pi/4)
    return integral

# Testing for different values of N
Ns = range(1, 50)
integral_values = [gauss_legendre_integral_b(N) for N in Ns]

# Plotting the result
plt.plot(Ns, integral_values)
plt.xlabel('N')
plt.ylabel('Integral Value')
plt.title('Convergence of Gauss-Legendre Quadrature for Integral (b)')
plt.show()
