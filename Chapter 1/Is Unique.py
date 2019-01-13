# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def isUnique(s):
    exist = []
    for i in range(len(s)):
        if s[i] in exist:
            return False
        else:
            exist.append(s[i])
    return True

