# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given 
# the "true" length of the string.

def URLify(s):
    s = list(s.strip())
    for i in range(len(s)):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)

