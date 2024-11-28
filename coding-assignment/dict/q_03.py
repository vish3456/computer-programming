'''Find the key of the maximum value in a dictionary.'''
my_dict = {"a": 10, "b": 25, "c": 15}
max_key = max(my_dict, key=my_dict.get)
print(max_key)
