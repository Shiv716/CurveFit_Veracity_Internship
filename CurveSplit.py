import numpy as np
import matplotlib.pyplot as plt

# Assuming you have your coordinates in x_data and y_data arrays
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([2, 5, 9, 15, 20, 22, 21, 18, 12, 8])

# Setting a freq of split
split_curve = 5

# Setting up the individual split resultant curves on the same graph (for each required array-list)
split_x = [x_data[i:i + split_curve] for i in range(0, len(x_data), split_curve)]
split_y = [y_data[i:i + split_curve] for i in range(0, len(y_data), split_curve)]

# Plotting all the parts of the same graph: -
plt.figure(figsize=(8, 6))
for chunk_x, chunk_y in zip(split_x, split_y):
    plt.plot(chunk_x, chunk_y, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Disintegrated curve')
plt.grid(True)
plt.show()