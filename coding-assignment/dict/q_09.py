'''Find all keys with the same value in a dictionary.'''
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
value_groups = {}

for k, v in my_dict.items():
    value_groups.setdefault(v, []).append(k)

print(value_groups)
