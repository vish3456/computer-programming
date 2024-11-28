''' Write a Function to Generate a Random Password'''
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print(generate_password(12))  # Output: Random 12-character password
