'''Check if an Element Exists in a Tuple'''
def element_exists(t, element):
    return element in t
print(element_exists((1, 2, 3, 4), 3))
print(element_exists((1, 2, 3, 4), 5))
