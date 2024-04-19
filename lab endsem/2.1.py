import numpy as np
import matplotlib.pyplot as plt

# Define the system of ODEs
def f(t, y):
    return np.array([y[1], -2*y[1] - 2*y[0]])

# Define the exact solution
def exact_sol(t):
    return np.exp(-t) * np.cos(t)

# Define the Runge-Kutta method
def rk3(t, h, y, f):
    k0 = h * f(t, y)
    k1 = h * f(t + h / 3, y + k0 / 3)
    k2 = h * f(t + 2 * h / 3, y + 2 * k1 / 3)
    return y + 1 / 4 * k0 + 3 / 4 * k2

# Set initial conditions
y0 = np.array([1, -1])
t0 = 0
h = 0.01
t_final = 2

# Initialize arrays to store the solution
t_values = np.arange(t0, t_final, h)
y_values = np.zeros((len(t_values), 2))
y_values[0] = y0

# Perform the integration
for i in range(len(t_values) - 1):
    y_values[i+1] = rk3(t_values[i], h, y_values[i], f)

# Plot the numerical solution
plt.plot(t_values, y_values[:, 0], label='Numerical solution')

# Plot the exact solution
t_exact = np.linspace(t0, t_final, 1000)
y_exact = exact_sol(t_exact)
plt.plot(t_exact, y_exact, label='Exact solution')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Print out each xi and yi, yi exact
for i in range(len(t_values)):
    print(f"xi = {t_values[i]}, yi = {y_values[i, 0]}, yi exact = {exact_sol(t_values[i])}")
