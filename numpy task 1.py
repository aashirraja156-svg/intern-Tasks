import numpy as np

# Create a simple array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Basic operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Reshape into a 2D matrix
matrix = arr.reshape(1, 5)  # 1 row, 5 columns
print("Reshaped Matrix:\n", matrix)

# Multiplication by scalar
print("Array * 2:", arr * 2)
