import numpy as np

class SchrageLCG:
    def __init__(self, seed, a=16807, m=(2**31) - 1):
        self.state = seed
        self.a = a
        self.m = m
        self.q = self.m // self.a
        self.r = self.m % self.a
    
    def random(self):
        # Schrage factorization to prevent overflow
        self.state = (self.a * (self.state % self.q) - self.r * (self.state // self.q)) % self.m
        return float(self.state) / self.m

def simple_lcg(seed, a=16807, m=(2**31) - 1):
    # Simple LCG, without Schrage factorization
    # This function returns a new seed and a random number
    new_seed = (a * seed) % m
    return new_seed, float(new_seed) / m

def metropolis_integral(rng, N=1000, delta=0.4, M=15):
    Z = 0.46265167
    if isinstance(rng, SchrageLCG):
        x = rng.random()  # initial x from random number generator (class)
    else:
        _, x = rng  # initial x from random number generator (function)
    
    samples = []
    for _ in range(N * M):
        if isinstance(rng, SchrageLCG):
            x_new = x + delta * (2 * rng.random() - 1)
        else:
            seed, random_number = rng
            x_new = x + delta * (2 * random_number - 1)
            rng = simple_lcg(seed)
        
        if 0 <= x_new <= 1:
            if np.random.random() < min(1, (np.exp(x_new**2) - 1) / (np.exp(x**2) - 1)):
                x = x_new
        if _ % M == 0:
            samples.append(x**2 / (np.exp(x**2) - 1))
    
    return Z * np.mean(samples)

# Ask user for which RNG to use
rng_choice = input("Choose the RNG method (Enter '1' for Schrage LCG, '2' for simple LCG): ")

seed = int(input("Enter a seed (positive integer): "))
N = int(input("Enter the number of sampling points N (e.g., 1000): "))

if rng_choice == '1':
    rng = SchrageLCG(seed)
else:
    # Start the simple LCG generator with the initial seed
    seed, _ = simple_lcg(seed)
    rng = simple_lcg(seed)

# Compute the integral
integral_value = metropolis_integral(rng, N=N)
print(f"The estimated value of the integral is {integral_value}")
