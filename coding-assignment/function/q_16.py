'''Write a Function to Check if a Number is Armstrong'''
def is_armstrong(num):
    digits = list(map(int, str(num)))
    return num == sum(d**len(digits) for d in digits)

print(is_armstrong(153))  # Output: True
print(is_armstrong(123))  # Output: False
