''' Count the frequency of words in a sentence using a dictionary'''
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
