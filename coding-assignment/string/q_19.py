''' Check if Two Strings are Rotations of Each Other'''
str1 = "abcd"
str2 = "cdab"
if len(str1) == len(str2) and str2 in str1 + str1:
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")
