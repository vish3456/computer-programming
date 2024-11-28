'''Find the Second Largest Element'''
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None
print(second_largest([5, 3, 8, 1, 8, 7]))
