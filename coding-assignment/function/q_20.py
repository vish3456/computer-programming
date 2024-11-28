'''Write a Function to Find All Divisors of a Number'''
def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(find_divisors(28))  # Output: [1, 2, 4, 7, 14, 28]
