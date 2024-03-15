import numpy as np
import random

def w(x):
    return np.exp(x**2) - 1

def g(x):
    return x**2 / (np.exp(x**2) - 1)

def metropolis(N, delta=0.4, M=15):
    samples = []
    x = random.random()  # initial x from uniform[0, 1]
    for _ in range(N * M):
        x_new = x + delta * (2 * random.random() - 1)  # proposed move
        if 0 <= x_new <= 1 and random.random() < min(1, w(x_new) / w(x)):
            x = x_new  # accept move with Metropolis criterion
        if _ % M == 0:
            samples.append(x)
    return np.mean([g(x) for x in samples])

# Z value is provided
Z = 0.46265167

# Compute the integral for various N
for N in [10, 100, 1000, 10000, 100000]:
    avg_g = metropolis(N)
    I = Z * avg_g
    print(f"N = {N}, Estimated Integral = {I}")
