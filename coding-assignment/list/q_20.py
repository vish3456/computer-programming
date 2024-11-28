''' Rotate a List by n Positions'''
# Solution
lst = [10, 20, 30, 40, 50]
n = 2
rotated = lst[n:] + lst[:n]
print("Rotated list:", rotated)
