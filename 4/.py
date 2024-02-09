import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import leggauss
from numpy.polynomial.laguerre import laggauss
from numpy.polynomial.hermite import hermgauss

# Function Definitions for Each Integral
def gauss_legendre_integral_a(N):
    x, w = leggauss(N)
    return sum(w * np.exp(-x**2))

def transform_b(x):
    return (np.pi/4) * (x + 1)

def gauss_legendre_integral_b(N):
    x, w = leggauss(N)
    xt = transform_b(x)
    return sum(w * np.log(1 + xt)) * (np.pi/4)

def gauss_laguerre_integral_c(N):
    x, w = laggauss(N)
    return sum(w * np.sin(x))

def gauss_laguerre_integral_d(N):
    x, w = laggauss(N)
    return sum(w * np.sqrt(x) / (x + 4))

def gauss_hermite_integral_e(N):
    x, w = hermgauss(N)
    return sum(w * np.sin(x)**2)

def gauss_hermite_integral_f(N):
    x, w = hermgauss(N)
    return sum(w / np.sqrt(1 + x**2))

# Range of N values
Ns = range(1, 20)

# Plotting
fig, axs = plt.subplots(3, 2, figsize=(12, 18))
fig.suptitle('Convergence of Gaussian Quadratures')

# Integral (a)
axs[0, 0].plot(Ns, [gauss_legendre_integral_a(N) for N in Ns])
axs[0, 0].set_title('Integral (a): Gauss-Legendre')

# Integral (b)
axs[0, 1].plot(Ns, [gauss_legendre_integral_b(N) for N in Ns])
axs[0, 1].set_title('Integral (b): Gauss-Legendre')

# Integral (c)
axs[1, 0].plot(Ns, [gauss_laguerre_integral_c(N) for N in Ns])
axs[1, 0].set_title('Integral (c): Gauss-Laguerre')

# Integral (d)
axs[1, 1].plot(Ns, [gauss_laguerre_integral_d(N) for N in Ns])
axs[1, 1].set_title('Integral (d): Gauss-Laguerre')

# Integral (e)
axs[2, 0].plot(Ns, [gauss_hermite_integral_e(N) for N in Ns])
axs[2, 0].set_title('Integral (e): Gauss-Hermite')

# Integral (f)
axs[2, 1].plot(Ns, [gauss_hermite_integral_f(N) for N in Ns])
axs[2, 1].set_title('Integral (f): Gauss-Hermite')

for ax in axs.flat:
    ax.set(xlabel='N', ylabel='Integral Value')

# for loop for grid for every plot
for ax in axs.flat:
    ax.grid()
# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
