import numpy as np

def trapezoidal_rule(f, a, b, n):
    """Compute the integral of `f` from `a` to `b` using the trapezoidal rule with `n` intervals."""
    h = (b - a) / n
    return (f(a) + f(b) + 2 * sum(f(a + i * h) for i in range(1, n))) * h / 2

def simpson_rule(f, a, b, n):
    """Compute the integral of `f` from `a` to `b` using Simpson's rule with `n` intervals."""
    if n % 2 == 1:
        raise ValueError("Simpson's rule requires an even number of intervals.")
    h = (b - a) / n
    return (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) +
            2 * sum(f(a + i * h) for i in range(2, n - 1, 2))) * h / 3

def romberg_integration(f, a, b, tolerance):
    """Compute the integral of `f` from `a` to `b` using Romberg integration with a specified `tolerance`."""
    R = [[(f(a) + f(b)) * (b - a) / 2.0]]
    n = 1
    while True:
        h = (b - a) / (2 ** n)
        trapezoid_est = 0.5 * R[n - 1][0] + h * sum(f(a + (k - 0.5) * h) for k in range(1, 2 ** n))
        R.append([trapezoid_est])
        for m in range(1, n + 1):
            extrapolated_val = R[n][m - 1] + (R[n][m - 1] - R[n - 1][m - 1]) / (4 ** m - 1)
            R[n].append(extrapolated_val)
        if abs(R[n][n] - R[n - 1][n - 1]) < tolerance:
            return R[n][n]
        n += 1
        if n == 10:  # Avoid infinite loops by setting a cap on iterations
            return R[n - 1][n - 1]

# Define a dictionary to map input strings to function objects
function_mapper = {
    'a': np.sin,
    'b': lambda x: np.exp(-x),
    'c': lambda x: 1 / (1 + x**2),
    'd': lambda x: 1 / x,
    'e': lambda x: np.sqrt(1 - (1 / 4) * np.sin(x)**2),
    'f': lambda x: 1 / (np.sin(x)**2 + (1 / 4) * np.cos(x)**2),
}

# Prompt the user for input parameters
function_input = input("Enter the function to integrate (e.g., 'a', 'b', 'c', 'd', 'e', 'f'): ")
method = input("Enter the method ('trapezoidal', 'simpson', 'romberg'): ")
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))

# Get the relevant parameters based on the chosen method
if method in ['trapezoidal', 'simpson']:
    n = int(input("Enter the number of intervals (spacing h will be calculated): "))
    if method == 'simpson' and n % 2 != 0:
        n += 1  # Ensure n is even for Simpson's rule
elif method == 'romberg':
    tolerance = float(input("Enter the desired tolerance: "))
else:
    raise ValueError("Invalid method chosen.")

# Retrieve the function to integrate from the function mapper
if function_input in function_mapper:
    f = function_mapper[function_input]
else:
    raise ValueError("Function not recognized.")

# Perform the integration and display the result
if method == 'trapezoidal':
    result = trapezoidal_rule(f, a, b, n)
elif method == 'simpson':
        result = simpson_rule(f, a, b, n)
elif method == 'romberg':
    result = romberg_integration(f, a, b, tolerance)
else:
    raise ValueError("Method not recognized.")

print(f"The integral of the selected function from {a} to {b} using {method} is: {result}")

