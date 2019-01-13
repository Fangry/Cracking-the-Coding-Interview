# - *- coding: utf- 8 - *-
# Given a string, write a function to check if it is a permutation of a palin­drome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is
# a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


def PalindPerm(s):
    charCount = {}
    for i in range(len(s)):
        if s[i] in charCount:
            charCount[s[i]] += 1
        else:
            charCount[s[i]] = 1

    if len(s) % 2 == 0:
        for c in charCount:
            if charCount[c] % 2 != 0:
                return False
        return True
    else:
        oddCount = 0
        for c in charCount:
            if charCount[c] % 2 != 0:
                oddCount += 1
                if oddCount == 2:
                    return False
        return True


