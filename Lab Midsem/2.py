#bernoulli's method
def bernoulli_method(f, df, x0, tolerance, max_iterations):
    x = x0
    for _ in range(max_iterations):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x

