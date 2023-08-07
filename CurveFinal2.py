import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x_data = np.array([1, 2, 3, 4, 5, 10])  # Replace this with your actual x-coordinates
y_data = np.array([2, 4, 6, 8, 10, 11])  # Replace this with your actual y-coordinates

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
print("Residuals "+str(residuals))
## Manage to set a threshold on this list, for bot vs human ^^

plt.figure(figsize=(12, 6))

# Plot the data and fitted line
plt.subplot(1, 2, 1)
plt.scatter(x_data, y_data, color='blue', label='Data')
plt.plot(x_data, y_pred, color='red', label='Fitted Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Regression Fit')
plt.legend()

# Plot the residuals
plt.subplot(1, 2, 2)
plt.scatter(x_data, residuals, color='green')
plt.axhline(y=0, color='red', linestyle='--', label='Residuals')
plt.xlabel('X-axis')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.legend()

plt.tight_layout()
plt.show()