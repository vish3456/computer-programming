''' Remove All Special Characters from a String'''
import re

string = "Hello! How's it going? @Python_123"
cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', string)
print("Cleaned String:", cleaned_string)
