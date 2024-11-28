'''Write a Function to Check if a String is a Valid Email Address'''
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email("example@gmail.com"))  # Output: True
print(is_valid_email("example.gmail.com"))  # Output: False
