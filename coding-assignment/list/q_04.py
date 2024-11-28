''' Find Even Numbers in a List'''
def find_even(lst):
    return [num for num in lst if num % 2 == 0]
print(find_even([1, 2, 3, 4, 5, 6]))
