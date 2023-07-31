import numpy as np
import matplotlib.pyplot as plt
import csv

# Set of coordinates
x = np.array([-1, -0.8, -0.7, -0.6, -0.55, -0.5, -0.4, -0.3, -0.2, 0, 0.3, 0.4, 0.6, 0.8, 0.85, 0.9, 1])
y = np.array([-1, -0.5, -0.4, -0.3, -0.2, -0.1, 0.15, 0.27, 0.38, 0.5, 0.7, 0.72, 0.75, 0.85, 0.87, 0.9, 1])

# Lists for RMSE values for different degrees
rmse_values = [] # for original coordinates
rmse_rot_values = [] # for rotated coordinates
deg_range = range(1, 50) # of the chebyshev polynomial

# Try different degrees and calculate the RMSE for each degree
for degree in deg_range:
    # Perform Chebyshev polynomial approximation
    coefficients = np.polynomial.chebyshev.Chebyshev.fit(x, y, degree)

    # Generate some x-values for evaluation
    x_eval = np.linspace(x[0], x[-1], 200)

    # Evaluate the Chebyshev polynomial at the given x-values
    y_approx = coefficients(x_eval)

    # Calculate the root mean square error (RMSE)
    rmse = np.sqrt(np.mean((y_approx - np.interp(x_eval, x, y)) ** 2))
    rmse_values.append(rmse)

# Find the degree with the smallest RMSE
best_degree = np.argmin(rmse_values) + 1

print("Best Degree:", best_degree)

# Perform Chebyshev polynomial approximation with the best degree
coefficients = np.polynomial.chebyshev.Chebyshev.fit(x, y, best_degree)

# Generate x-values for evaluation
x_eval = np.linspace(x[0], x[-1], 200)

# Evaluate the Chebyshev polynomial at the given x-values
y_approx = coefficients(x_eval)


# Find rotation angle

one_deg = np.polynomial.chebyshev.Chebyshev.fit(x, y, 1)

x_one_deg = np.linspace(x[0], x[-1], 200)
y_one_deg = one_deg(x_one_deg)
dx = np.max(x_one_deg) - np.min(x_one_deg)
dy = np.max(y_one_deg) - np.min(y_one_deg)

rotation_angle = np.arctan2(dy, dx)

# use rotation angle to find the rotation matrix
rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                            [np.sin(rotation_angle), np.cos(rotation_angle)]])
rotated_trajectory = np.dot(np.column_stack((x, y)), rotation_matrix)

x_list, y_list = np.split(rotated_trajectory, 2, axis=1)

# Try different degrees and calculate the RMSE for each degree for the rotated data
for degree in deg_range:
    # Perform Chebyshev polynomial approximation
    coefficients_rot = np.polynomial.chebyshev.Chebyshev.fit(x_list.flatten(), y_list.flatten(), degree)

    # Generate some x-values for evaluation
    #x_eval_rot = np.linspace(x[0], x[-1], 200)  # Use 200 points for evaluation
    x_eval_rot = np.linspace(np.min(rotated_trajectory[:, 0]), np.max(rotated_trajectory[:, 0]), 200)

    # Evaluate the Chebyshev polynomial at the given x-values
    y_approx_rot = coefficients_rot(x_eval_rot)

    # Calculate the root mean square error (RMSE)
    rmse_rot = np.sqrt(np.mean((y_approx_rot - np.interp(x_eval_rot, x_list.flatten(), y_list.flatten())) ** 2))
    rmse_rot_values.append(rmse_rot)

# Find the degree with the smallest RMSE for the rotated data
best_degree_rot = np.argmin(rmse_rot_values) + 1

print("Best Rotation Degree:", best_degree_rot)

# Fit Chebyshev polynomial to the rotated data
coefficients_rot = np.polynomial.chebyshev.Chebyshev.fit(x_list.flatten(), y_list.flatten(), best_degree_rot)

# Generate x-values for evaluation
x_eval_rotat = np.linspace(rotated_trajectory[0, 0], rotated_trajectory[-1, 0], 200)

# Evaluate the Chebyshev polynomial at the given x-values
y_final_rot = coefficients_rot(x_eval_rotat)

# Plot of unrotated and rotated points with corresponding chebyshev fitted polynomials
plt.scatter(x, y, label="Original Trajectory", color='red')
plt.plot(x_eval, y_approx, label="Best Fit (Degree {})".format(best_degree), color='blue')
plt.plot(x_one_deg, y_one_deg, label="One-Degree Polynomial Approximation", color='green', linestyle='dashed')
plt.scatter(rotated_trajectory[:, 0], rotated_trajectory[:, 1], label="Rotated Trajectory", color='green')
plt.plot(x_eval_rotat, y_final_rot, label="Best Fit (Degree {})".format(best_degree_rot), color='orange')
plt.xlabel('x coordinates')
plt.ylabel('y coordinates')
plt.title('Chebyshev Polynomial Fitting Trial')
plt.legend()
plt.show()

# Saving rmse results to a csv file
csv_filename = "results.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Degree", "Unrotated RMSE", "Rotated RMSE", "Best Fit"])
    for degree, rmse_unrot, rmse_rot in zip(deg_range, rmse_values, rmse_rot_values):
        best_fit_label = "Unrotated" if rmse_unrot < rmse_rot else "Rotated"
        writer.writerow([degree, rmse_unrot, rmse_rot, best_fit_label])

# Plot of unrotated vs rotated RMSE values
plt.plot(deg_range, rmse_values, label="Unrotated RMSE", color='blue')
plt.plot(deg_range, rmse_rot_values, label="Rotated RMSE", color='green')
plt.xlabel('Degree')
plt.ylabel('RMSE Value')
plt.title('Comparison of rotated vs unrotated RMSE values')
plt.legend()
plt.show()
