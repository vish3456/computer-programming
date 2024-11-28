'''Find the Second Largest Number in a List'''
# Solution
nums = [12, 34, 56, 78, 89, 67]
unique_nums = list(set(nums))
unique_nums.sort()
second_largest = unique_nums[-2]
print("Second largest:", second_largest)
