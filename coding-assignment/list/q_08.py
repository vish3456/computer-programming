''' Find Common Elements in Two Lists'''
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
