import numpy as np
import matplotlib.pyplot as plt

# Assuming you have your coordinates in x_data and y_data arrays
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = np.array([2, 5, 9, 15, 20, 22, 21, 18, 12, 8])

threshold = 6  # Define your threshold value here

# Function to split data into chunks based on threshold
def split_into_chunks(x_data, y_data, threshold):
    chunks_x = []
    chunks_y = []
    current_chunk_x = [x_data[0]]
    current_chunk_y = [y_data[0]]

    for i in range(1, len(x_data)):
        distance = np.sqrt((x_data[i] - x_data[i-1])**2 + (y_data[i] - y_data[i-1])**2)
        if distance > threshold:
            chunks_x.append(current_chunk_x)
            chunks_y.append(current_chunk_y)
            current_chunk_x = [x_data[i]]
            current_chunk_y = [y_data[i]]
        else:
            current_chunk_x.append(x_data[i])
            current_chunk_y.append(y_data[i])

    chunks_x.append(current_chunk_x)
    chunks_y.append(current_chunk_y)

    return chunks_x, chunks_y

chunks_x, chunks_y = split_into_chunks(x_data, y_data, threshold)

# Plotting each chunk separately
plt.figure(figsize=(8, 6))
for chunk_x, chunk_y in zip(chunks_x, chunks_y):
    plt.plot(chunk_x, chunk_y, marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Splitting Curve into Chunks')
plt.grid(True)
plt.show()