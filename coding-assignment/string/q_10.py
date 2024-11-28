'''Count the Occurrence of Each Character in a String'''
def char_count(s):
    return {char: s.count(char) for char in set(s)}
print(char_count("hello"))
