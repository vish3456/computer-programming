''' Remove Negative Numbers from a List'''
def remove_negatives(lst):
    return [num for num in lst if num >= 0]
print(remove_negatives([-1, 2, -3, 4, 5, -6]))
