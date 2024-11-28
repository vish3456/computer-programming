'''Update multiple keys in a dictionary at once.
'''
my_dict = {"a": 1, "b": 2, "c": 3}
updates = {"b": 20, "c": 30, "d": 40}
my_dict.update(updates)
print(my_dict)
