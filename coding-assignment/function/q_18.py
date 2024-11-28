''' Write a Function to Find the Longest Word in a List of Words'''
def longest_word(words):
    return max(words, key=len)

print(longest_word(["apple", "banana", "cherry", "watermelon"]))  # Output: watermelon
