'''Combine two dictionaries and sum values of common keys.'''
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 40}

combined_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
print(combined_dict)
