'''Split a List into Even and Odd Numbers'''
# Solution
nums = [10, 15, 20, 25, 30, 35]
even = [n for n in nums if n % 2 == 0]
odd = [n for n in nums if n % 2 != 0]
print("Even:", even)
print("Odd:", odd)
