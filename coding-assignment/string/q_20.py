'''Find the Most Frequent Character in a String'''
string = "programming"
most_frequent = max(set(string), key=string.count)
print("Most Frequent Character:", most_frequent)
