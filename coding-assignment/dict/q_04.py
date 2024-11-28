'''Remove all key-value pairs where the value is less than 10.
'''
my_dict = {"a": 5, "b": 15, "c": 8, "d": 20}
filtered_dict = {k: v for k, v in my_dict.items() if v >= 10}
print(filtered_dict)
