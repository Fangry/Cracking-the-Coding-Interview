# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to
# check if they are one edit (or zero edits) away.


def oneOrZeroAway(s1, s2):
    if s1 == s2:
        return True
    diff = len(s1) - len(s2)
    if diff > 1 and diff < -1:
        return False
    elif diff == 0:
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count == 2:
                    return False
        return True
    elif diff == 1:
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                if s1[i+1] != s2[i]:
                    return False
        return True
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] != s2[i+1]:
                    return False
        return True
