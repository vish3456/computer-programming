''' Find the First Non-Repeating Character'''
string = "swiss"
for char in string:
    if string.count(char) == 1:
        print("First non-repeating character:", char)
        break
