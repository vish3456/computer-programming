''' Find All Substrings of a String'''
string = "abc"
substrings = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
print("Substrings:", substrings)
