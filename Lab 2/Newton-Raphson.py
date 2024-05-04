import numpy as np
import random

# Example of newton raphson with an example function
f = lambda x: x**2 + 5x + 1
f_prime = lambda x: 2x + 5
x0 = 2
tolerance = 1e-7

def newton_raphson (f, f_prime, x0, tolerance):
    if abs(f(x0)) < tolerance:
        return x0
    else:
        return newton_raphson (f, f_prime, x0 - f(x0)/f_prime(x0), tolerance)

newton_raphson (f, f_prime, x0, tolerance)

#calling the same newton_raphson with a random number
x0 = random.random()

newton_raphson (f, f_prime, x0, tolerance)