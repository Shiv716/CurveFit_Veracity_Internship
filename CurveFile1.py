"""
@Author Shivang Chaudhary
"""

import numpy as np
from matplotlib import pyplot as plt


# Considering input data to be of array format...
# ... Prototype file: -

# Verifying the input to be valid tuple of numbers
#if type(val) != float:
 #   raise Exception("Please input valid numbers encased in '()'")


# Functions for usage
#def getFunction(x, a, b, c):
 #   return a * x**2 + b * x + c


# Supposed input coordinate array
c = np.array([1, 2, 3, 4, 5])

# Procuring chebyshev coefficients of array
cheb = np.polynomial.chebyshev.Chebyshev(c)
coef = np.polynomial.chebyshev.cheb2poly(cheb.coef)
print("The coefficients to the polynomial are: " + str(coef))

# Warping the coefficients in 0-1 list [For future use, if needed.]
binaryVector = np.where(coef > 0.5, 1, 0)
print(binaryVector)


# Plotting the graph of input coordinates
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(1, 10, 50)
plt.plot(c, c="red")
plt.plot(coef, c="blue")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Chebyshev Curve')
plt.show()


# Terminating the program
exit()