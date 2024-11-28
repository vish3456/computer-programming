'''Flatten a Nested List'''
# Solution
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened)
