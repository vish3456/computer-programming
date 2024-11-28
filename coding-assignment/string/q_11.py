'''Find All Permutations of a String'''
from itertools import permutations

string = "abc"
perms = [''.join(p) for p in permutations(string)]
print("Permutations:", perms)
