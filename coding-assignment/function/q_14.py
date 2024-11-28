'''Write a Function to Count Uppercase and Lowercase Letters in a String'''
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

upper_count, lower_count = count_case("Hello World!")
print("Uppercase:", upper_count)  # Output: 2
print("Lowercase:", lower_count)  # Output: 8
