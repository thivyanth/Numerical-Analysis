
# Importing necessary libraries
import math

# Define the equations and their derivatives
def equation1(x):
    return math.atan(x)-1  # Placeholder equation

def equation2(x):
    return x**3 + 2*x**2 +10*x-20 # Placeholder equation

def equation3(x):
    return math.cos(x)-x  # Placeholder equation

def equation4(x):
    return  math.tan(x) - 1/(1+x**2)# Placeholder equation

# derivatives
def derivative1(x):
    return 1 / (1 + x**2)

def derivative2(x):
    return 3*x**2 + 4*x + 10

def derivative3(x):
    return -math.sin(x) - 1

def derivative4(x):
    return (1 / math.cos(x))**2 + 2*x / ((1 + x**2)**2)

# Add derivatives for equations 3 and 4 here

# Newton's Method
def newtons_method(f, df, x0, tolerance, max_iterations):
    x = x0
    for _ in range(max_iterations):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x

# Bisection Method
def bisection_method(f, a, b, tolerance, max_iterations):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    for _ in range(max_iterations):
        mid = (a + b) / 2
        if f(mid) == 0 or (b - a) / 2 < tolerance:
            return mid
        if f(mid) * f(a) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

# Modified False Position Method
def modified_false_position_method(f, a, b, tolerance, max_iterations):
    for _ in range(max_iterations):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        if abs(f(c)) < tolerance:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Main program
def main():
    equations = [equation1, equation2, equation3, equation4]  # Add other equations here
    derivatives = [derivative1, derivative2, derivative3, derivative4]  # Add other derivatives here
    methods = {
        'Newton': newtons_method,
        'Bisection': bisection_method,
        'Modified False Position': modified_false_position_method
    }

    # User input for method
    print("Select a method: Newton, Bisection, Modified False Position")
    method = input().strip()

    # User input for equation
    print("Select an equation (1-4):")
    eq_num = int(input().strip()) - 1

    # Additional parameters based on method
    if method == 'Newton':
        print("Enter initial guess:")
        x0 = float(input().strip())
        print("Enter tolerance:")
        tolerance = float(input().strip())
        print("Enter maximum iterations:")
        max_iterations = int(input().strip())
        result = methods[method](equations[eq_num], derivatives[eq_num], x0, tolerance, max_iterations)
    else:
        print("Enter lower bound:")
        a = float(input().strip())
        print("Enter upper bound:")
        b = float(input().strip())
        print("Enter tolerance:")
        tolerance = float(input().strip())
        print("Enter maximum iterations:")
        max_iterations = int(input().strip())
        result = methods[method](equations[eq_num], a, b, tolerance, max_iterations)
    
    print("The result is:", result)

if __name__ == "__main__":
    main()
