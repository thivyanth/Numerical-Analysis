import numpy as np

def newtons_method(x, y, X):
    n = len(x)
    diff = np.zeros((n, n))
    diff[:,0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff[i, j] = (diff[i + 1, j - 1] - diff[i, j - 1]) / (x[i + j] - x[i])

    result = y[0]
    for i in range(1, n):
        term = diff[0, i]
        for j in range(i):
            term *= (X - x[j])
        result += term

    return result

def lagrange_method(x, y, X):
    result = 0.0
    n = len(x)
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (X - x[j]) / (x[i] - x[j])
        result += term
    return result

def aitken_method(x, y, X):
    n = len(x)
    P = np.copy(y)
    for k in range(1, n):
        for i in range(n - k):
            P[i] = ((X - x[i + k]) * P[i] + (x[i] - X) * P[i + 1]) / (x[i] - x[i + k])
    return P[0]

# Main function
def main():
    methods = {'1': newtons_method, '2': lagrange_method, '3': aitken_method}
    print("Choose interpolation method:\n1. Newton's Fundamental Formula\n2. Lagrange Interpolation\n3. Aitken's Iterative Interpolation")
    method_choice = input("Enter choice (1/2/3): ")

    n = int(input("Enter the order of interpolation (n): "))
    X = float(input("Enter the value of x for interpolation: "))

    h = 1.0 / n
    x = np.array([i * h for i in range(n + 1)])
    y = np.cos(x)

    if method_choice in methods:
        interpolated_value = methods[method_choice](x, y, X)
        actual_value = np.cos(X)
        print(f"Interpolated value at x = {X}: {interpolated_value}")
        print(f"Actual value of cos({X}): {actual_value}")
    else:
        print("Invalid method choice.")

if __name__ == "__main__":
    main()
