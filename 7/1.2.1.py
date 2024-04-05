import numpy as np
import matplotlib.pyplot as plt

def rk4(f, x0, y0, h, xmax):
    """ Fourth-Order Runge-Kutta method """
    x = np.arange(x0, xmax + h, h)
    y = np.zeros((len(x), len(y0)))
    y[0, :] = y0
    print(f"Step 0: x = {x[0]:.2f}, y1 = {y[0, 0]:.4f}, y2 = {y[0, 1]:.4f}")

    for i in range(1, len(x)):
        k1 = h * f(x[i-1], y[i-1, :])
        k2 = h * f(x[i-1] + 0.5*h, y[i-1, :] + 0.5*k1)
        k3 = h * f(x[i-1] + 0.5*h, y[i-1, :] + 0.5*k2)
        k4 = h * f(x[i-1] + h, y[i-1, :] + k3)
        y[i, :] = y[i-1, :] + (k1 + 2*k2 + 2*k3 + k4) / 6
        print(f"Step {i}: x = {x[i]:.2f}, y1 = {y[i, 0]:.4f}, y2 = {y[i, 1]:.4f}")

    return x, y

def taylor_method(f, x0, y0, h, xmax):
    """ Simplified Fourth-Order Taylor method (using only first derivative) """
    x = np.arange(x0, xmax + h, h)
    y = np.zeros((len(x), len(y0)))
    y[0, :] = y0
    print(f"Step 0: x = {x[0]:.2f}, y1 = {y[0, 0]:.4f}, y2 = {y[0, 1]:.4f}")

    for i in range(1, len(x)):
        dy = f(x[i-1], y[i-1, :])
        y[i, :] = y[i-1, :] + h * dy
        print(f"Step {i}: x = {x[i]:.2f}, y1 = {y[i, 0]:.4f}, y2 = {y[i, 1]:.4f}")

    return x, y

def system_equations(x, y):
    """ System of first-order ODEs from the given second-order ODE """
    y1, y2 = y
    dy1dx = y2
    dy2dx = x - y2 - y1**2
    return np.array([dy1dx, dy2dx])

def plot_results(x, y_rk4, y_taylor, method):
    plt.figure(figsize=(10, 5))
    if method == 'rk4':
        plt.plot(x, y_rk4[:, 0], label='y1 RK4', linestyle='-', color='blue')
        plt.plot(x, y_rk4[:, 1], label='y2 RK4', linestyle='--', color='blue')
    elif method == 'taylor':
        plt.plot(x, y_taylor[:, 0], label='y1 Taylor', linestyle='-', color='red')
        plt.plot(x, y_taylor[:, 1], label='y2 Taylor', linestyle='--', color='red')
    plt.title(f'Solution of Differential Equations using {method.capitalize()} method')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

# User input
method = input("Choose the method (RK4 or Taylor): ").strip().lower()
h = float(input("Enter the step size h: "))
xmax = float(input("Enter the maximum value of x (xmax): "))
x0 = 0
y0 = np.array([1, 0])  # Initial conditions

# Solve using chosen method
if method == 'rk4':
    x, y_method = rk4(system_equations, x0, y0, h, xmax)
elif method == 'taylor':
    x, y_method = taylor_method(system_equations, x0, y0, h, xmax)
else:
    raise ValueError("Invalid method selected. Use 'RK4' or 'Taylor'.")

# Plotting the results
plot_results(x, y_method, y_method, method)
