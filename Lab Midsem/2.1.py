import numpy as np

# Coefficients of the polynomial
a0, a1, a2, a3, a4 = 1, -5, 9, -7, 2

# Initial guess for the root
x_k = 1.0

# Number of iterations for convergence
iterations = 10

# Applying Bernoulli's method
roots = []
for _ in range(iterations):
    # Calculate the next estimate using Bernoulli's formula
    r_k = (a1*x_k**3 + a2*x_k**2 + a3*x_k + a4) / (a0*x_k**4)
    x_k_plus_1 = r_k * x_k
    roots.append(x_k_plus_1)

    # Update the current estimate
    x_k = x_k_plus_1

# The last computed root is our best estimate
dominant_root = roots[-1]

# Output the numerical value of the dominant root
print(dominant_root)
