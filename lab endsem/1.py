import numpy as np

def monte_carlo_integral(rng, N=1000):
    f = lambda x, y: np.sin(np.pi / 2 * (x + y))
    I = 0

    for _ in range(N):
        x, y = rng.random(), rng.random()
        I += f(x, y)
    return I / N

class simple_lcg:
    def __init__(self, seed, a=69069, m=(2**31) - 1, b=23375):
        self.seed = seed
        self.a = a
        self.m = m
        self.b = b
    def random(self):
        self.seed = (self.a * self.seed + self.b) % self.m
        return float(self.seed) / self.m

print(monte_carlo_integral(simple_lcg(12345), N=1000000))