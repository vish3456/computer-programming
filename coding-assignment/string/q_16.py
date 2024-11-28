'''Count the Occurrences of Each Word in a String'''
sentence = "this is a test this is only a test"
words = sentence.split()
word_count = {word: words.count(word) for word in set(words)}
print("Word Frequency:", word_count)
