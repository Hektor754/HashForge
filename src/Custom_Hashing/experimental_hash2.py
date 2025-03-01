import random
import numpy as np
import math

# Fibonacci function (you can adjust as per your needs)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_hashing(text):
    hash_value = 0x1234567890abcdef1234567890abcdef
    length = len(text)
    matrices = []

    # Finding valid (x, y) for matrix dimensions
    for i in range(1, length + 1):
        if length % i == 0:  # Check if length is divisible by i
            y2 = length // i  # Calculate y2 as length divided by i
            y = int(math.sqrt(y2))  # Calculate the square root of y2
            if y * y == y2:  # Check if y^2 is equal to y2 (perfect square)
                x = i  # Set x to i and y to the calculated y
                break

    if x is None or y is None:
        raise ValueError("No valid (x, y) configuration found.")  # Ensure x and y are valid

    print(f"Found valid (x, y): {x}, {y}")
    
    # Convert text to ASCII values
    ascii_values = [ord(char) for char in text]

    # Create matrices of size (y, y)
    for i in range(x):
        start = i * y ** 2
        end = start + y ** 2
        matrix = np.array(ascii_values[start:end]).reshape(y, y)
        matrices.append(matrix)

    # Multiply all matrices together
    result_matrix = matrices[0]
    for matrix in matrices[1:]:
        result_matrix = np.dot(result_matrix, matrix)

    # Flatten the result matrix and calculate the sum
    flattened_matrix = result_matrix.flatten()
    hash_process = sum(flattened_matrix)

    # Reduce hash_process to a manageable size, e.g., using modulo
    hash_process = hash_process % 1000000  # Modulo operation to reduce the value

    # Apply Fibonacci to the reduced result
    hash_value = fibonacci(hash_process)

    # Ensure the hash is always 256 bits (64 characters in hexadecimal)
    fixed_size_hash = f"{hash_value:032x}"  # Make sure it's at least 32 characters long
    fixed_size_hash = fixed_size_hash[:64]  # Truncate or slice to 64 characters (256 bits)

    return fixed_size_hash

# Test
text = "Lets Try This One More Time"
hash_value = fib_hashing(text)
print(f"Final fixed-size hash value: {hash_value}")