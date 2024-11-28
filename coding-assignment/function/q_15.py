'''Write a Function to Return Fibonacci Sequence up to n Terms'''
def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
