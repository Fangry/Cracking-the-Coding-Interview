# Given two strings, write a method to decide if one is a permutation of the other.

def checkPerm(s1, s2):
    s2l = list(s2)
    for i in range(len(s1)):
        contain = False
        for j in range(len(s2l)):
            if s1[i] == s2l[j]:
                del s2l[j]
                contain = True
                break
        if not contain:
            return False
    if not s2l:
        return True
    else:
        return False
        