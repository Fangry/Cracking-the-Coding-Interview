'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''


def strCompress(s):
    if len(s) == 0:
        return s
    ns = []
    i, count = 0, 1

    while i < len(s)-1:
        if s[i] == s[i+1]:
            count += 1
        else:
            ns.extend((s[i], count))
            count = 1
        i += 1
    if count > 0:
        ns.extend((s[i], count))
    if len(s) > len(ns):
        return ''.join(map(str, ns))
    else:
        return s
