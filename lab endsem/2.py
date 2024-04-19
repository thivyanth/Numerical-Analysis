import numpy as np
import matplotlib.pyplot as plt
def rk3(f, y0, t):
    """ 
    3rd order Runge-Kutta method to solve ODEs
    f : function
        Function that defines the differential equation
    y0 : float
        Initial condition
    t : array
        Array of time points where the solution is computed
    Returns
    -------
    y : 1D array
        Approximation y(t[i]) of the solution at the points t
    """
    y = np.zeros(len(t))
    for i in range(0, len(t) - 1):
        h = t[i+1] - t[i]
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + h/2, y[i] + k1/2)
        k3 = h * f(t[i] + h, y[i] - k1 + 2*k2)
        y[i+1] = y[i] + (k1 + 4*k2 + k3) / 6
    return y
    y[0] = y0

def system_equations(x, y):
    """ System of first-order ODEs from the given second-order ODE """
    y1, y2 = y
    dy1dx = y2
    dy2dx = x - y2 - y1**2
    return np.array([dy1dx, dy2dx])

#rk3
def rk3(f, x0, y0, h, xmax):
    """ Third-Order Runge-Kutta method """
    x = np.arange(x0, xmax + h, h)
    y = np.zeros((len(x), len(y0)))
    y[0, :] = y0
    print(f"Step 0: x = {x[0]:.2f}, y1 = {y[0, 0]:.4f}, y2 = {y[0, 1]:.4f}")

    for i in range(1, len(x)):
        k1 = h * f(x[i-1], y[i-1, :])
        k2 = h * f(x[i-1] + 0.5*h, y[i-1, :] + 0.5*k1)
        k3 = h * f(x[i-1] + h, y[i-1, :] - k1 + 2*k2)
        y[i, :] = y[i-1, :] + (k1 + 4*k2 + k3) / 6
        print(f"Step {i}: x = {x[i]:.2f}, y1 = {y[i, 0]:.4f}, y2 = {y[i, 1]:.4f}")

    return x, y

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

# method = input("Choose the method (RK4 or Taylor): ").strip().lower()
h = 0.001
xmax = 10
x0 = 0
y0 = np.array([1, 0]) 

x, y_method = rk3(system_equations, x0, y0, h, xmax)
plot_results(x, y_method, y_method, method='rk4')
# consider the 2nd order ode y''+2y'+2y=0
# with y(0)=1 and y'(0)=-1 as the initial conditions.
# Use the 3rd order Runge-Kutta method to solve the ODE
# k1 = hF(xi+1/3 h, yi + 1/3 k0)
# k2 = hF(xi+2/3 h, yi + 2/3 k1)
# yi+1 = yi + 1/4 k0 + 3/4 k2
# the exact solution of the ODE is y(x) = e^(-x)cos(x)
# Plot the exact solution and the numerical solution
# print out each xi and yi, yi exact
# you have to convert the second order ode to a system of first order odes