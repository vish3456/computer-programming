''' Write a Function to Find the GCD of Two Numbers'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # Output: 6

