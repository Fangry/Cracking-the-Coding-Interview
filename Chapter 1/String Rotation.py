'''
Assume you have a method isSubstringwhich checks if one word is a substring of another. 
Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
Method: Concenate s1 to itself (twice the length) and try to find s2 in it.
'''


def isSubstring(s1, s2):
    len1, len2 = len(s1), len(s2)
    if len2 > len1:
        return False
    for i in range(len1 - len2 + 1):
        isSubstr = True
        for j in range(len2):
            if s1[i + j] != s2[j]:
                isSubstr = False
                break
        if isSubstr:
            return True
    return False


def strRotate(s1, s2):
    if len(s1) == len(s2):
        return isSubstring(s1 + s1, s2)
    return False
