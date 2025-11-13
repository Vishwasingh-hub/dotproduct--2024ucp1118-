import numpy as np

# Define two vectors as NumPy arrays
vector_a = np.array([1, 2, 3, 4, 5])
vector_b = np.array([6, 7, 8, 9, 10])

# Calculate the dot product
dot_product_result = np.dot(vector_a, vector_b)
# Alternatively, using the @ operator:
# dot_product_result = vector_a @ vector_b

# Bug fix from main: print fixed result
print(f"Fixed Dot Product: {dot_product_result}")

# Extra info from parallel branch
print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}")
print(f"Dot Product: {dot_product_result}")

# Add a temporary debug print
print("Debug: starting dot product calculation")


