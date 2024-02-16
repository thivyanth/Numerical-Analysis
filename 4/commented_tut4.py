import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss  # Gauss-Legendre quadrature
from numpy.polynomial.laguerre import laggauss  # Gauss-Laguerre quadrature
from numpy.polynomial.hermite import hermgauss  # Gauss-Hermite quadrature

# Define functions to compute integrals using Gaussian quadrature

def gauss_legendre_integral_a(N):
    # Gauss-Legendre quadrature for integral of exp(-x^2)
    x, w = leggauss(N)  # Get N points and weights for the quadrature
    return sum(w * np.exp(-x**2))  # Compute the weighted sum

def transform_b(x):
    # Transformation function for integral (b)
    return (np.pi/4) * (x + 1)

def gauss_legendre_integral_b(N):
    # Gauss-Legendre quadrature with a coordinate transformation
    x, w = leggauss(N)
    xt = transform_b(x)  # Apply transformation to quadrature points
    return sum(w * np.log(1 + xt)) * (np.pi/4)  # Compute the weighted sum with transformed points

def gauss_laguerre_integral_c(N):
    # Gauss-Laguerre quadrature for integral of sin(x)
    x, w = laggauss(N)
    return sum(w * np.sin(x))

def gauss_laguerre_integral_d(N):
    # Gauss-Laguerre quadrature for integral of sqrt(x) / (x + 4)
    x, w = laggauss(N)
    return sum(w * np.sqrt(x) / (x + 4))

def gauss_hermite_integral_e(N):
    # Gauss-Hermite quadrature for integral of sin(x)^2
    x, w = hermgauss(N)
    return sum(w * np.sin(x)**2)

def gauss_hermite_integral_f(N):
    # Gauss-Hermite quadrature for integral of 1 / sqrt(1 + x^2)
    x, w = hermgauss(N)
    return sum(w / np.sqrt(1 + x**2))

# Define a range of N values for comparison
Ns = range(1, 20)

# Calculate converged values for each integral using higher N
converged_a = gauss_legendre_integral_a(50)
# ... same for b, c, d, e, f

# Plotting
fig, axs = plt.subplots(3, 2, figsize=(12, 18))
fig.suptitle('Convergence of Gaussian Quadratures')

# Plot for each integral
# ... plotting code for each integral

# Common settings for all plots
for ax in axs.flat:
    ax.set(xlabel='N', ylabel='Integral Value')
    ax.grid()

# Adjust layout and show plot
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
