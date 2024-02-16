import numpy as np

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
        
def main():
    n = int(input("Enter N (~10 is recommended): "))
    X = float(input("Enter the value of x for interpolation: "))

    h = 1.0 / n  
    x = np.array([i * h for i in range(n + 1)]) 
    y = np.cos(x)

    interpolated_value = lagrange_method(x, y, X)
    actual_value = np.cos(X)
    print(f"Interpolated value at x = {X}: {interpolated_value}")
    print(f"Actual value of cos({X}): {actual_value}")

if __name__ == "__main__":
    main()
