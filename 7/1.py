import numpy as np

def f(x, y):
    # y[0] = y1, y[1] = y2
    return np.array([y[1], x - y[1] - y[0]**2])

def taylor_series_step(x, y, h):
    # We need to calculate up to the fourth derivative terms
    # For demonstration, we're assuming some simplistic derivatives (more complex derivatives require symbolic computing)
    f0 = f(x, y)
    f1 = np.array([f0[1], 1 - f0[1] - 2*y[0]*f0[0]])  # First derivative approximation
    f2 = np.array([f1[1], -f1[1] - 2*f0[0]*f0[0] - 2*y[0]*f1[0]])  # Second derivative approximation
    f3 = np.array([f2[1], -f2[1] - 4*f0[0]*f1[0] - 2*y[0]*f2[0]])  # Third derivative approximation

    # Taylor expansion
    y_next = y + f0*h + f1*(h**2)/2 + f2*(h**3)/6 + f3*(h**4)/24
    return y_next

def rk4_step(x, y, h):
    k1 = f(x, y)
    k2 = f(x + 0.5*h, y + 0.5*h*k1)
    k3 = f(x + 0.5*h, y + 0.5*h*k2)
    k4 = f(x + h, y + h*k3)
    y_next = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    return y_next

def solve_ode(method, h, x_max):
    x = 0
    y = np.array([1.0, 0.0])  # Initial conditions
    steps = int(x_max / h)
    result = np.zeros((steps + 1, 3))  # To store (x, y1, y2)
    result[0, :] = [x, y[0], y[1]]

    for i in range(1, steps + 1):
        if method == 'taylor':
            y = taylor_series_step(x, y, h)
        elif method == 'rk4':
            y = rk4_step(x, y, h)
        x += h
        result[i, :] = [x, y[0], y[1]]

    return result

if __name__ == "__main__":
    method = input("Enter the method (taylor/rk4): ").strip().lower()
    h = float(input("Enter the step size h: "))
    x_max = float(input("Enter the maximum value of x (x_max): "))

    solution = solve_ode(method, h, x_max)
    for step in solution:
        print(f"x = {step[0]:.4f}, y1 = {step[1]:.4f}, y2 = {step[2]:.4f}")
