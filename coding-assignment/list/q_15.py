'''Remove Duplicates From a List'''
# Solution
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(dict.fromkeys(items))
print("Unique items:", unique_items)
