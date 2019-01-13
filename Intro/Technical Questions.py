# p79 unnescessary work demonstration: Print all positive integer solutions
# to the equation a^3 + b^3 = c^3 + d^3
# time complexity: 1st ex. O(n^4), 2nd ex. O(n^3), 3rd ex. O(n^2)


def abcd1(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                for d in range(1, n):
                    if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3):
                        print(a, b, c, d)
                        break  # bc. there'is only one solution


def abcd2(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                d = (pow(a, 3) + pow(b, 3) - pow(c, 3))**1/3
                if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3):
                    print(a, b, c, d)
                    break


def abcd3(n):
    ab = {}
    for a in range(1, n):
        for b in range(1, n):
            ab[pow(a, 3) + pow(b, 3)] = a, b
    for c in range(1, n):
        for d in range(1, n):
            result = pow(c, 3) + pow(d, 3)
            if result in ab:
                print(ab[result][0], ab[result][1], c, d)


# p82, Design an algorithm to print all permutations of a string.
# For simplicity, assume all cha racters are unique

def permStr(s):
    if len(s) == 1:
        print(s)
        return
    for i in range(len(s)):
        c = s[i]
        withoutC = s[:i] + s[i+1:]
        for j in range(len(withoutC)):
            print(withoutC[:j] + c + withoutC[j:])
        permStr(withoutC)


# p84 Best Conceivable Runtime (BCR)
# Given two sorted arrays, find the number of elements in common
# The arrays are the same length and each has all distinct elements
# You know BCR is O(A + B) bc. you have to look at every element in two lists at least once
# 1st ex. O(n^2), 2nd ex. O(N)

def bcr1(low, high, n):
    import random
    a, b = random.sample(range(low, high), n), random.sample(
        range(low, high), n)
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                count += 1
    return count


def bcr2(low, high, n):
    import random
    a, b = random.sample(range(low, high), n), random.sample(
        range(low, high), n)
    return len(set(a) & set(b))


