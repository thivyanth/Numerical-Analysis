import math

# Define the equations for which we want to find the roots
def equation1(x):
    # atan(x) - 1
    return math.atan(x) - 1

def equation2(x):
    # x^3 + 2x^2 + 10x - 20
    return x**3 + 2*x**2 + 10*x - 20 

def equation3(x):
    # cos(x) - x
    return math.cos(x) - x 

def equation4(x):
    # tan(x) - 1 / (1 + x^2)
    return math.tan(x) - 1 / (1 + x**2)

# Define the derivatives of each equation
def derivative1(x):
    # Derivative of atan(x) - 1 is 1 / (1 + x^2)
    return 1 / (1 + x**2)

def derivative2(x):
    # Derivative of x^3 + 2x^2 + 10x - 20 is 3x^2 + 4x + 10
    return 3*x**2 + 4*x + 10

def derivative3(x):
    # Derivative of cos(x) - x is -sin(x) - 1
    return -math.sin(x) - 1

def derivative4(x):
    # Derivative of tan(x) - 1 / (1 + x^2) involves complex calculations
    return (1 / math.cos(x))**2 + 2*x / ((1 + x**2)**2)

# Newton's Method for finding roots
def newtons_method(f, df, x0, tolerance, max_iterations):
    x = x0  # Start with initial guess
    for _ in range(max_iterations):
        x_new = x - f(x) / df(x)  # Newton's iteration formula
        if abs(x_new - x) < tolerance:  # Check if we are close enough to the root
            return x_new
        x = x_new
    return x  # Return the approximate root

# Bisection Method for finding roots
def bisection_method(f, a, b, tolerance, max_iterations):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        # If the function has the same sign at both ends, no root is bracketed
        return "Interval does not bracket a root."

    for _ in range(max_iterations):
        mid = (a + b) / 2  # Middle point
        f_mid = f(mid)
        if abs(f_mid) < tolerance or (b - a) / 2 < tolerance:
            # If middle point is close enough to root or interval is sufficiently small
            return mid

        # Narrow down the interval to the half where the root lies
        if fa * f_mid < 0:
            b, fb = mid, f_mid
        else:
            a, fa = mid, f_mid

# Modified False Position Method for finding roots
def modified_false_position_method(f, a, b, tolerance, max_iterations):
    fa, fb = f(a), f(b)

    for _ in range(max_iterations):
        c = b - fb * (b - a) / (fb - fa)  # Calculate the new point
        fc = f(c)

        if abs(fc) < tolerance:
            # If new point is close enough to root
            return c

        # Update the interval and halve the function value on the side that is not being narrowed
        if fa * fc < 0:
            b, fb = c, fc
            fa /= 2
        else:
            a, fa = c, fc
            fb /= 2

    return (a + b) / 2  # Return the approximate root if no exact root is found within max_iterations

# Main program
def main():
    # List of equations and their derivatives
    equations = [equation1, equation2, equation3, equation4]
    derivatives = [derivative1, derivative2, derivative3, derivative4]

    # Dictionary of methods for finding roots
    methods = {
        'Newton': newtons_method,
        'Bisection': bisection_method,
        'Modified False Position': modified_false_position_method
    }

    # Ask the user if they want to solve all equations automatically
    print("Should I solve all four equations with different methods automatically? (y/n)")
    auto_run = input().strip().lower() == 'y'

    if auto_run:
        # Define common parameters for all methods
        tolerance = 0.001
        max_iterations = 100
        newton_guesses = [1, 1, 0, 0]  # Initial guesses for Newton's method
        bounds = (0, 10)  # Bounds for Bisection and Modified False Position methods

        print("Solving all equations with each method:")
        print("{:<10} {:<30} {:<30} {:<30}".format("Equation", "Newton's Method", "Bisection Method", "Modified False Position"))
        for i, eq in enumerate(equations, start=1):
            results = []
            # Apply each method to each equation
            results.append(methods['Newton'](eq, derivatives[i-1], newton_guesses[i-1], tolerance, max_iterations))
            results.append(methods['Bisection'](eq, *bounds, tolerance, max_iterations))
            results.append(methods['Modified False Position'](eq, *bounds, tolerance, max_iterations))
            # Print the results
            print("{:<10} {:<30} {:<30} {:<30}".format("Equation " + str(i), *results))

        print("The predetermined correct answers are 1.557, 1.369, 0.739, (0.624, 3.229, or 6.308)")
    else:
        # For individual method selection and equation
        print("Select a method: Newton, Bisection, Modified False Position")
        method = input().strip()

        print("Select an equation (1-4):")
        eq_num = int(input().strip()) - 1

        # User inputs for the selected method
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
