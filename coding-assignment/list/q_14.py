''' Check if a List is a Palindrome'''
# Solution
lst = [1, 2, 3, 2, 1]
if lst == lst[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
