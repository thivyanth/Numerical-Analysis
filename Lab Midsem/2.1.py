from sympy import symbols, Poly

# Define the symbol
x = symbols('x')

# Define the polynomial
polynomial = x**4 - 5*x**3 + 9*x**2 - 7*x + 2

# Get coefficients of the polynomial
poly_obj = Poly(polynomial)
a0, a1, a2, a3, a4 = poly_obj.all_coeffs()

# Initial guess for the root
x_k = 1

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

# Evaluate to get a numerical value
numerical_value = dominant_root.evalf()
print()
