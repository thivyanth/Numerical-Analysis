import numpy as np

# Define the trapezoidal rule
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    return (f(a) + f(b) + 2 * sum(f(a + i * h) for i in range(1, n))) * h / 2

# Define Simpson's rule
def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("Simpson's rule requires an even number of intervals.")
    h = (b - a) / n
    return (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) +
            2 * sum(f(a + i * h) for i in range(2, n-1, 2))) * h / 3

# Define the Romberg integration
def romberg_integration(f, a, b, tolerance):
    R = [[(f(a) + f(b)) * (b - a) / 2.0]]  # R[0][0] with one trapezoidal step
    n = 1
    while True:
        # Compute the next row with trapezoidal estimates with 2^n steps
        h = (b - a) / (2 ** n)
        trapezoid_est = 0.5 * R[n-1][0] + h * sum(f(a + (k - 0.5) * h) for k in range(1, 2 ** n))
        R.append([trapezoid_est])
        
        # Compute the Richardson extrapolation values
        for m in range(1, n + 1):
            extrapolated_val = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4 ** m - 1)
            R[n].append(extrapolated_val)
        
        # Check for convergence
        if abs(R[n][n] - R[n-1][n-1]) < tolerance:
            return R[n][n]
        
        n += 1

    # If max iterations are reached without convergence, return the last computed value
    return R[-1][-1]


# Define a function mapper
function_mapper = {
    'a': np.sin,
    #e^-x
    'b': lambda x: np.exp(-x),
    #1/1+x^2
    'c': lambda x: 1/(1+x**2),
    #1/x
    'd': lambda x: 1/x,
    #sqrt[(1-1/4)sin^2x
    'e': lambda x: np.sqrt((1-((1/4)*np.sin(x)**2))),
    #1/(sin^2x+1/4 cos^2x)
    'f': lambda x: 1/(np.sin(x)**2+1/4*np.cos(x)**2),
}

# User input for the function, method, limits, and spacing or tolerance
function_input = input("Enter the function to integrate (e.g., 'a', 'b', 'c', 'd', 'e', 'f'): ")
method = input("Enter the method ('trapezoidal', 'simpson', 'romberg'): ")
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
if method in ['trapezoidal', 'simpson']:
    n = int(input("Enter the number of intervals (spacing h will be calculated): "))
else:
    tolerance = float(input("Enter the desired tolerance: "))

# Map the input to the actual function
if function_input not in function_mapper:
    raise ValueError("Function not recognized.")
f = function_mapper[function_input]

# Perform the integration using the selected method
if method == 'trapezoidal':
    result = trapezoidal_rule(f, a, b, n)
elif method == 'simpson':
    result = simpson_rule(f, a, b, n)
elif method == 'romberg':
    result = romberg_integration(f, a, b, tolerance)
else:
    raise ValueError("Method not recognized.")

print(f"The integral of {function_input} from {a} to {b} using {method} is: {result}")
