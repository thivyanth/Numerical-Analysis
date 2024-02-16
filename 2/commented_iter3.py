import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Newton's method for interpolation
def newtons_method(x, y, X):
    n = len(x)  # Number of data points
    diff = np.zeros((n, n))  # Initialize a matrix to store divided differences
    diff[:,0] = y  # First column is y values

    # Calculate divided differences
    for j in range(1, n):
        for i in range(n - j):
            diff[i, j] = (diff[i + 1, j - 1] - diff[i, j - 1]) / (x[i + j] - x[i])

    # Calculate interpolated value at X using Newton's formula
    result = y[0]
    for i in range(1, n):
        term = diff[0, i]
        for j in range(i):
            term *= (X - x[j])
        result += term

    return result

# Lagrange method for interpolation
def lagrange_method(x, y, X):
    result = 0.0
    n = len(x)  # Number of data points

    # Calculate interpolated value at X using Lagrange's formula
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (X - x[j]) / (x[i] - x[j])
        result += term
    return result

# Aitken's iterative method for interpolation
def aitken_method(x, y, X):
    n = len(x)  # Number of data points
    P = np.copy(y)  # Copy y values to start the process

    # Aitken's iterative formula to find interpolated value
    for k in range(1, n):
        for i in range(n - k):
            P[i] = ((X - x[i + k]) * P[i] + (x[i] - X) * P[i + 1]) / (x[i] - x[i + k])
    return P[0]

# Function to generate interpolation plots
def generate_plots(x, y, methods, X):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'ko', label='Original Points')  # Plot original data points
    x_vals = np.linspace(min(x), max(x), 1000)  # Generate points for interpolation

    # Plot interpolated values for each method
    for name, method in methods.items():
        y_vals = np.array([method(x, y, x_val) for x_val in x_vals])
        plt.plot(x_vals, y_vals, label=name)
    plt.plot(X, np.cos(X), 'r*', label='Actual Value')  # Plot actual value at X
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Interpolation Comparison')
    plt.show()

# Function to perform interpolation using all methods and display in table
def perform_all_interpolations(x, y, X):
    methods = {'Newton': newtons_method, 'Lagrange': lagrange_method, 'Aitken': aitken_method}
    results = []
    
    # Apply each method and store results
    for name, method in methods.items():
        interpolated_value = method(x, y, X)
        results.append([name, interpolated_value, np.cos(X)])
    df = pd.DataFrame(results, columns=['Method', 'Interpolated Value', 'Actual Value'])
    print(df)

# Manual interpolation function
def manual_interpolation():
    methods = {'1': newtons_method, '2': lagrange_method, '3': aitken_method}
    print("Choose interpolation method:\n1. Newton's Fundamental Formula\n2. Lagrange Interpolation\n3. Aitken's Iterative Interpolation")
    method_choice = input("Enter choice (1/2/3): ")

    n = int(input("Enter the order of interpolation (n): "))
    X = float(input("Enter the value of x for interpolation: "))

    h = 1.0 / n  # Calculate step size
    x = np.array([i * h for i in range(n + 1)])  # Generate x values
    y = np.cos(x)  # Generate y values (cos(x))

    # Perform chosen interpolation method
    if method_choice in methods:
        interpolated_value = methods[method_choice](x, y, X)
        actual_value = np.cos(X)
        print(f"Interpolated value at x = {X}: {interpolated_value}")
        print(f"Actual value of cos({X}): {actual_value}")
    else:
        print("Invalid method choice.")
        
# Main function to run the program
def main():
    print("Choose option:")
    print("1. Default setting (Table of cos(x) interpolation using all methods)")
    print("2. Manual interpolation choice")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        n = int(input("Enter the order of interpolation (n): "))
        X = float(input("Enter the value of x for interpolation: "))
        h = 1.0 / n
        x = np.array([i * h for i in range(n + 1)])
        y = np.cos(x)
        perform_all_interpolations(x, y, X)
    elif choice == '2':
        manual_interpolation()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
