import numpy as np

# Differential equation
def F(x, y):
    return x + y

# Exact solution
def y_exact(x):
    return np.exp(x) - x - 1

# Euler method
def euler_method(h, x_max):
    x = np.arange(0, x_max + h, h)
    y = np.zeros(len(x))
    for i in range(1, len(x)):
        y[i] = y[i-1] + h * F(x[i-1], y[i-1])
    return x, y

# Fourth-order Taylor expansion
def taylor_method(h, x_max):
    x = np.arange(0, x_max + h, h)
    y = np.zeros(len(x))
    for i in range(1, len(x)):
        y[i] = y[i-1] + h * F(x[i-1], y[i-1]) + \
               (h**2 / 2) * (1 + F(x[i-1], y[i-1])) + \
               (h**3 / 6) * (1 + F(x[i-1], y[i-1])) + \
               (h**4 / 24) * (1 + F(x[i-1], y[i-1]))
    return x, y

# Fourth-order Runge-Kutta method
def runge_kutta_method(h, x_max):
    x = np.arange(0, x_max + h, h)
    y = np.zeros(len(x))
    for i in range(len(x) - 1):
        k0 = h * F(x[i], y[i])
        k1 = h * F(x[i] + h/2, y[i] + k0/2)
        k2 = h * F(x[i] + h/2, y[i] + k1/2)
        k3 = h * F(x[i] + h, y[i] + k2)
        y[i + 1] = y[i] + (k0 + 2*k1 + 2*k2 + k3) / 6
    return x, y

# Main program
def solve_ode():
    h = float(input("Enter step size h: "))
    x_max = float(input("Enter maximum value of x (x_max): "))
    method = input("Choose the method (euler/taylor/runge_kutta): ")
    
    if method == 'euler':
        x, y = euler_method(h, x_max)
    elif method == 'taylor':
        x, y = taylor_method(h, x_max)
    elif method == 'runge_kutta':
        x, y = runge_kutta_method(h, x_max)
    else:
        print("Invalid method.")
        return
    
    for i in range(len(x)):
        print(f"x = {x[i]:.4f}, y = {y[i]:.4f}, y_exact = {y_exact(x[i]):.4f}")

# Uncomment the following line to run the program
solve_ode()
