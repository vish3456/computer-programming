'''Check if a String is a Substring of Another'''
def is_substring(s, sub):
    return sub in s
print(is_substring("hello world", "world"))
print(is_substring("hello world", "python"))
