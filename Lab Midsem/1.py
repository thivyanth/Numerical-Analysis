import math

def f(x):
    return (math.cos(x))**2 -2*x+3
def df(x):
    return (-math.sin(2*x)-2)
def d2f(x):
    return (-2*math.cos(2*x))
def lamberts_method(f, df, d2f, x0, tolerance, max_iterations):
    x = x0  # Start with initial guess
    for _ in range(max_iterations):
        x_new = x - f(x) / (df(x)-f(x)*d2f(x)/(2*df(x)))  # Lambert's iteration formula
        if abs(x_new - x) < tolerance:  # Check if we are close enough to the root
            return x_new
        x = x_new
    return x  # Return the approximate root
print(lamberts_method(f,df,d2f,x0=1,tolerance=0.000001, max_iterations=5000))