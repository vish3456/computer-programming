''' Sort a dictionary by its values.'''
my_dict = {"a": 30, "b": 10, "c": 20}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
