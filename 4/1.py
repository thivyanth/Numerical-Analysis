import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss

def gauss_legendre_integral_a(N):
    x, w = leggauss(N)
    integral = sum(w * np.exp(-x**2))
    return integral

# Testing for different values of N
Ns = range(1, 50)  # You can adjust the range as needed
integral_values = [gauss_legendre_integral_a(N) for N in Ns]

# Plotting the result
plt.plot(Ns, integral_values)
plt.xlabel('N')
plt.ylabel('Integral Value')
plt.title('Convergence of Gauss-Legendre Quadrature for Integral (a)')
plt.show()
