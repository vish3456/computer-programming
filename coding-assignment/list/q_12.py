'''Count Frequency of Each Element in a List'''
# Solution
elements = [1, 2, 2, 3, 3, 3, 4, 5, 5]
frequency = {}
for item in elements:
    frequency[item] = frequency.get(item, 0) + 1
print(frequency)
