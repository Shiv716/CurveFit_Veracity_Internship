import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression


# Building the quadratic curve to fit on the graph: -
def quadratic_function(x, a, b, c):
    return a * x ** 2 + b * x + c


# Trial pair of coordinates: -
# PAIR-1
#x = np.array([1, 2, 3, 4, 5])
#y = np.array([2, 5, 9, 15, 20])

# PAIR-2
#x = np.array([1, 2, 3, 4, 5, 78, 90, 100, 119, 120, 150])
#y = np.array([2, 5, 9, 15, 20, 67, 89, 91, 78, 89, 100])

# PAIR-3
#x = np.array([1, 25, 100, 250])
#y = np.array([4, 2, 7, 9])

# PAIR-4
x = np.array([0, 15, 5, 89, 10])
y = np.array([2, 1, 3, 50, 2])


# Input coordinates (choose (x,y) from above): -
x_data = x
y_data = y
print('x coordinates: ' + str(x))
print('y coordinates: ' + str(y))

# Fitting the curve: -
popt, _ = curve_fit(quadratic_function, x_data, y_data)

# Generate the results: -
a_fit, b_fit, c_fit = popt
equation = f'y = {a_fit:.2f}x^2 + {b_fit:.2f}x + {c_fit:.2f}'
y_fit = quadratic_function(x_data, a_fit, b_fit, c_fit)

# Print the equation of the graph: -
print("The equation: " + equation)

# FOR GETTING THE RESIDUAL GRAPH: -
# Reshape the data to 2D arrays
x_data_reshaped = x_data.reshape(-1, 1)
y_data_reshaped = y_data.reshape(-1, 1)

# Fit a linear regression model
reg = LinearRegression()
reg.fit(x_data_reshaped, y_data_reshaped)

# Get the predicted values
y_pred = reg.predict(x_data_reshaped)

# Calculate the residuals
residuals = y_data_reshaped - y_pred
print("Residuals:- \n" + str(residuals))


# TRACK the 'residual' elements: -
thresholdValue = 0  # Initialising the variable that can be used as threshold for complete data..
for i in range(0, residuals.size):
    if residuals[i] > 1 or residuals[i] < -1:
        # print("check i: "+str(i))
        thresholdValue = thresholdValue + 1

# Use the loop to print out the conviction: -
print("Verify the threshold: " + str(thresholdValue))
if thresholdValue > 1 and thresholdValue > -1:
    print("The given data is HUMAN.")
else:
    print("The given data is BOT.")


# PLOTTING ALL THE GRAPHS: -
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(x_data, y_data, color='blue', label='Data')
plt.plot(x_data, y_fit, color='red', label='Fitted Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Quadratic fit')
plt.legend()
plt.grid(True)

# Plotting the residuals: -
plt.subplot(1, 2, 2)
plt.scatter(x_data, residuals, color='green', label='Residual-elements')
plt.axhline(y=0, color='red', linestyle='--', label='Residual-threshold')
plt.xlabel('X-axis')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.legend()

plt.tight_layout()
plt.show()