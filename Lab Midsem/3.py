import numpy as np

def forward_difference_4(f, a, b, n=4):
    h = (b - a) / n 
    # return (f(a) + f(b) + 2 * sum(f(a + i * h) for i in range(1, n))) * h / 2
    return (f(a) + f(b) + 2 * (f(a + h) + f(a + 2*h) + f(a + 3*h))) * h / 2

def f(x):
    return (1-0.5*np.sin(x)**2)
print(forward_difference_4(f,0,np.pi/2))