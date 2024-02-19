import sympy as sp
import numpy as np


# Define the function to integrate
def f(x):
    return 1 - 0.5 * sp.sin(x)**2

# Implement the Newton's forward difference formula for integration
def newtons_forward_difference_integration(a, b, n):
    # Calculate the width of each interval
    h = (b - a) / n
    # Initialize the sum
    integral_sum = 0
    # Calculate the values using the formula
    for i in range(0, n, 3):  # N must be a multiple of 3
        x0 = a + i * h
        f0 = f(x0)
        f1 = f(x0 + h)
        f2 = f(x0 + 2*h)
        f3 = f(x0 + 3*h)
        integral_sum += (3 * h / 8) * (f0 + 3 * f1 + 3 * f2 + f3)
    return integral_sum

# Function to find the appropriate N and integrate
def integrate_to_accuracy(a, b, desired_accuracy):
    # Start with N as a multiple of 3
    N = 3
    while True:
        result = newtons_forward_difference_integration(a, b, N)
        # Check if the result is accurate to four decimal places
        if round(result, 4) == round(desired_accuracy, 4):
            return result, N
        N += 3  # Increase N by multiples of 3

# The interval of integration from the problem
a = 0
b = sp.pi / 2
# The desired accuracy
desired_accuracy = 1.1781

# Find the N that gives the desired accuracy and the result of integration
result, N = integrate_to_accuracy(a, b, desired_accuracy)
print(result, N)
