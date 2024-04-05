import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0          # Length of the domain
t_max = 1.0      # Maximum time
N = 100           # Number of spatial divisions
M = 20000        # Number of time divisions
h = L / N        # Spatial step size
k = t_max / M    # Time step size
sigma = 0.5      # Stability parameter, sigma = k/h^2

# Stability check
if (1 - 2*sigma) < 0:
    print("Warning: Stability condition (1 - 2*sigma >= 0) not met!")

# Meshgrid creation
x = np.linspace(0, L, N+1)
t = np.linspace(0, t_max, M+1)

# Initial and boundary conditions
u = np.zeros((N+1, M+1))       # Initialize the solution array
u[:, 0] = np.sin(np.pi * x)    # Set the initial condition u(x,0) = sin(pi*x)

# Finite Difference Scheme (Explicit)
for m in range(0, M):  # Time steps
    for n in range(1, N):  # Spatial steps, excluding boundaries
        u[n, m+1] = sigma * u[n+1, m] + (1 - 2*sigma) * u[n, m] + sigma * u[n-1, m]
    # Boundary conditions: u(0, t) = u(L, t) = 0, automatically maintained

# Exact solution
u_exact = np.sin(np.pi * x[:, np.newaxis]) * np.exp(-np.pi**2 * t)

# Plotting the results
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.imshow(u, extent=[0, t_max, 0, L], origin='lower', aspect='auto')
plt.colorbar(label='Temperature')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Numerical Solution of Heat Equation')

plt.subplot(1, 2, 2)
plt.imshow(u_exact, extent=[0, t_max, 0, L], origin='lower', aspect='auto')
plt.colorbar(label='Temperature')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Exact Solution of Heat Equation')

plt.tight_layout()
plt.show()
