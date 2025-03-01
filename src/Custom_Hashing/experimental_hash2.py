import random
import numpy as np
import math

# Fibonacci function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_hashing(text):
    hash_value = 0x1234567890abcdef1234567890abcdef
    length = len(text)
    matrices = []

    # Finding valid (x,y) for matrix dimensions
    for i in range(1, length + 1):
        if length % i == 0:
            y2 = length // i
            y = int(math.sqrt(y2))
            if y * y == y2:
                x = i
                break

    if x is None or y is None:
        raise ValueError("No valid (x, y) configuration found.")

    print(f"Found valid (x, y): {x}, {y}")
    
    # Convert text to ASCII values
    ascii_values = [ord(char) for char in text]

    # Create matrices of size (y,y)
    for i in range(x):
        start = i * y ** 2
        end = start + y ** 2
        matrix = np.array(ascii_values[start:end]).reshape(y, y)
        matrices.append(matrix)

    # Multiply all matrices together
    result_matrix = matrices[0]
    for matrix in matrices[1:]:
        result_matrix = np.dot(result_matrix, matrix)

    flattened_matrix = result_matrix.flatten()
    hash_process = sum(flattened_matrix)

    # Reduce hash_process to a manageable size
    hash_process = hash_process % 1000000

    hash_value = fibonacci(hash_process)

   
    fixed_size_hash = f"{hash_value:032x}"
    fixed_size_hash = fixed_size_hash[:64]

    return fixed_size_hash

text = "Lets Try This One More Time"
hash_value = fib_hashing(text)
print(f"Final fixed-size hash value: {hash_value}")
