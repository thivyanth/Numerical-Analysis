import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(func, a, b, n):
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)
    fx = func(x)
    return h * (0.5 * fx[0] + np.sum(fx[1:-1]) + 0.5 * fx[-1])

def romberg_integration(trapezoidal_values):
    n = len(trapezoidal_values)
    R = np.zeros((n, n))
    R[:, 0] = trapezoidal_values

    for j in range(1, n):
        for i in range(j, n):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R

# Integral of sin(x) from 0 to pi/2
func = np.sin
a = 0
b = np.pi / 2
points = [4, 8, 16, 32]

# Calculate trapezoidal rule values
trapezoidal_values = [trapezoidal_rule(func, a, b, n) for n in points]

# Generate Romberg table
romberg_table = romberg_integration(trapezoidal_values)

# Plotting
plt.figure(figsize=(10, 6))
for i in range(len(points)):
    plt.plot([j for j in range(i + 1)], romberg_table[i, :i + 1], marker='o', label=f'{points[i]} points')

plt.axhline(y=1, color='r', linestyle='--', label='True Value (1)')
plt.title('Convergence of Romberg Integration')
plt.xlabel('Romberg Iteration')
plt.ylabel('Approximated Value')
plt.legend()
plt.grid(True)
plt.show()
