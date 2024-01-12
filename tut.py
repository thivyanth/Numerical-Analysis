
import math

def equation1(x):
    return math.atan(x)-1

def equation2(x):
    return x**3 + 2*x**2 +10*x-20 

def equation3(x):
    return math.cos(x)-x 

def equation4(x):
    return  math.tan(x) - 1/(1+x**2)

# derivatives
def derivative1(x):
    return 1 / (1 + x**2)

def derivative2(x):
    return 3*x**2 + 4*x + 10

def derivative3(x):
    return -math.sin(x) - 1

def derivative4(x):
    return (1 / math.cos(x))**2 + 2*x / ((1 + x**2)**2)


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
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        return "Interval does not bracket a root."

    # Main loop of the bisection method
    for _ in range(max_iterations):
        mid = (a + b) / 2
        f_mid = f(mid)

        # Check if we've found the root or are close enough
        if abs(f_mid) < tolerance or (b - a) / 2 < tolerance:
            return mid

        # Decide the side to apply bisection
        if fa * f_mid < 0:
            b, fb = mid, f_mid
        else:
            a, fa = mid, f_mid

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

    # Ask the user if they want automatic processing
    print("Should I solve all four equations with different methods automatically? (y/n)")
    auto_run = input().strip().lower() == 'y'

    if auto_run:
        tolerance = 0.001
        max_iterations = 100
        newton_guesses = [1, 1, 0, 0]
        bounds = (0, 10)  # Lower bound 0, upper bound 2

        print("Solving all equations with each method:")
        print("{:<10} {:<30} {:<30} {:<30}".format("Equation", "Newton's Method", "Bisection Method", "Modified False Position"))
        for i, eq in enumerate(equations, start=1):
            results = []
            results.append(methods['Newton'](eq, derivatives[i-1], newton_guesses[i-1], tolerance, max_iterations))
            results.append(methods['Bisection'](eq, *bounds, tolerance, max_iterations))
            results.append(methods['Modified False Position'](eq, *bounds, tolerance, max_iterations))
            print("{:<10} {:<30} {:<30} {:<30}".format("Equation " + str(i), *results))
            
        print("The predetermined correct answers are 1.557, 1.369, 0.739, (0.624, 3.229, or 6.308)")
    else:
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
