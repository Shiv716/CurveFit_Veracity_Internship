"""
@Author Shivang Chaudhary
"""

import numpy as np
import matplotlib.pyplot as plt

# Plotting the polynomial curve on supposed data points:-

x = [1,3,4,5,6,7]
y = [4,2,3,5,6,9]

# Setting the degree of the curve along with the points
curve_poly = np.polyfit(x,y,2)
poly_final = np.poly1d(curve_poly)

final_x = []
final_y = []

# Putting up the polynomial function: -
for i in range(20):
    final_x.append(i+1)
    element = poly_final(i+1)
    final_y.append(element)

# Plotting the graph: -
plt.plot(final_x,final_y)
plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Fitted Curve')
plt.show()