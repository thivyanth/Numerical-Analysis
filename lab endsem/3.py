# function f(A,N) of a matrix A as sum of A^i/i! for i=0 to N (basically the exponential of a matrix)
# write a program to calculate f(A,N) for a given matrix A (n by n) and integer N 

import numpy as np
from scipy.linalg import expm

def f(A, N):
    # Initialize the result matrix as an identity matrix
    res = np.identity(len(A))
    
    # Compute the sum of A^i/i! for i=1 to N
    for i in range(1, N+1):
        res += np.linalg.matrix_power(A, i) / np.math.factorial(i)
    
    return res

# Test the function with a sample matrix A and integer N
A = np.array([[1, 2], [3, 4]])
N = 10
print("Result from our function:\n", f(A, N))

# Cross check with scipy's expm function
print("Result from scipy's expm function:\n", expm(A))
