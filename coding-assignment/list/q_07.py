''' Check if a List is Sorted'''
def is_sorted(lst):
    return lst == sorted(lst)
print(is_sorted([1, 2, 3, 4]))
print(is_sorted([1, 3, 2, 4]))
