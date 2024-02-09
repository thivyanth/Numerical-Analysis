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

# Calculate converged values for each integral
converged_a = gauss_legendre_integral_a(50)
converged_b = gauss_legendre_integral_b(50)
converged_c = gauss_laguerre_integral_c(50)
converged_d = gauss_laguerre_integral_d(50)
converged_e = gauss_hermite_integral_e(20)  # Adjust as needed
converged_f = gauss_hermite_integral_f(20)  # Adjust as needed

# Plotting
fig, axs = plt.subplots(3, 2, figsize=(12, 18))
fig.suptitle('Convergence of Gaussian Quadratures')

# Integral (a)
integral_values_a = [gauss_legendre_integral_a(N) for N in Ns]
axs[0, 0].plot(Ns, integral_values_a, label=f'Converged: {converged_a:.6f}')
axs[0, 0].set_title('Integral (a): Gauss-Legendre')
axs[0, 0].legend()

# Integral (b)
integral_values_b = [gauss_legendre_integral_b(N) for N in Ns]
axs[0, 1].plot(Ns, integral_values_b, label=f'Converged: {converged_b:.6f}')
axs[0, 1].set_title('Integral (b): Gauss-Legendre')
axs[0, 1].legend()

# Integral (c)
integral_values_c = [gauss_laguerre_integral_c(N) for N in Ns]
axs[1, 0].plot(Ns, integral_values_c, label=f'Converged: {converged_c:.6f}')
axs[1, 0].set_title('Integral (c): Gauss-Laguerre')
axs[1, 0].legend()

# Integral (d)
integral_values_d = [gauss_laguerre_integral_d(N) for N in Ns]
axs[1, 1].plot(Ns, integral_values_d, label=f'Converged: {converged_d:.6f}')
axs[1, 1].set_title('Integral (d): Gauss-Laguerre')
axs[1, 1].legend()

# Integral (e)
integral_values_e = [gauss_hermite_integral_e(N) for N in Ns]
axs[2, 0].plot(Ns, integral_values_e, label=f'Converged: {converged_e:.6f}')
axs[2, 0].set_title('Integral (e): Gauss-Hermite')
axs[2, 0].legend()

# Integral (f)
integral_values_f = [gauss_hermite_integral_f(N) for N in Ns]
axs[2, 1].plot(Ns, integral_values_f, label=f'Converged: {converged_f:.6f}')
axs[2, 1].set_title('Integral (f): Gauss-Hermite')
axs[2, 1].legend()

# Common settings for all plots
for ax in axs.flat:
    ax.set(xlabel='N', ylabel='Integral Value')
    ax.grid()

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
