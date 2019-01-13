# p62 ex.11 factorial
# two ways, 1st uses recursion, 2nd uses while loop
# factorial1 - time complexity: O(n), space complexity: O(n)
# facorial 2 - time complexity: O(n), space complexity: O(1)


def factorial1(n):
    if n == 0:
        return 1
    else:
        return n*factorial1(n-1)


def factorial2(n):
    product = 1
    counter = n
    while counter > 1:
        product *= counter
        counter -= 1
    return product


# p62 ex.12 string permutation
# print all perm. of a string, the prefix of the string remains unchanged
# temp computes the string without the ith char, and that ith char is put in different places
# time complexity: O(n^2 * n!) as upper bound, it's not a tight bound, as there can be duplicate char in string which shortens runtime
# n represents number of char?


def permutation(string, prefix):
    if len(string) == 0:
        print(prefix)
    else:
        for i in range(len(string)):
            temp = string[0:i] + string[i+1:]
            # print(temp, prefix + string[i])
            permutation(temp, prefix + string[i])


# p64 ex.14 Fibonacci sequence
# print all fib numbers up to n
# time complexity: O(2^n), it's not O(n*2^n) because n is changing
# 2^1 + 2^2 + ... + 2^n = 2^(n+1), which is basically 2^n


def allFib(n):
    for i in range(n):
        def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
        print(i, ': ', fib(i))


# p64 ex.15 Storing Fibonacci sequence in list
# if a fib is already calculated, the function look it up in the list and use it to find the next fib
# time complexity: O(n), function takes constant time, technique call memoization
# this is much more efficient then ex.14

lst = {}


def fibList(n):
    if n in lst:
        # print('case 1: in lst')
        return lst[n]

    elif n < 2:
        # print('case 2: return ', n)
        return n

    else:
        temp = fibList(n-1) + fibList(n-2)
        # print('case 3: return', temp)
        lst[n] = temp
        return temp

# for i in range(1, 10):
#     print(i, ': ', fibList(i))


# p65 ex.16 print all power of 2 till number n
# each 'layer' is 2 times the previous n
# time complexity might not even increase when n is increased, n must double for runtime to increase
# time complexity: O(log n), divide n till it gets down to base case of 1

def pow2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = pow2(n/2)
        curr = prev*2
        print(curr)
        return curr

# p67 VI.2 computes a^b
# time complexity: O(b) for both functions


def power1(a, b):
    if b == 0:
        return 1
    else:
        return a * pow(a, b-1)


def power2(a, b):
    temp = a
    if b == 0:
        return 1
    elif b < 0:
        while b != -1:
            a /= temp
            b += 1
    else:
        while b != 1:
            a *= temp
            b -= 1
    return a

# p67 VI.3 computes a%b, use the that Python omit floating point in integer division
# time complexity: O(1)


def mod(a, b):
    if b == 0:
        return -1
    div = a/b
    return a - div*b

# p67 VI.4 computes a/b, using only addition and while loop
# basically says "how many times you add b can the sum be equal to a"
# time complexity: O(a/b)


def div(a, b):
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count += 1
    return count

# p67 VI.5 computes square root of n in integer (midpoint method)
# if n isn't perfect square, output -1
# time complexity: O(log n), function is basically binary search, halving the search with each run


def intSqrt1_run(n):
    return intSqrt1(n, 1, n)


def intSqrt1(n, low, high):
    if low > high:
        return -1
    guess = (low+high)/2
    print(low, high, guess)
    if guess**2 == n:
        return guess
    elif guess ** 2 < n:
        return intSqrt1(n, guess+1, high)
    else:
        return intSqrt1(n, low, guess-1)

# p67  VI.6 computes square root of n in integer (brute force method)
# VI.5 is more efficient, but VI.6 is simpler
# time complexity: O(sqrt(n))


def intSqrt2(n):
    counter = 1
    while counter <= n:
        if counter**2 == n:
            return counter
        else:
            counter += 1
    return -1


# p68 VI.10 adds all digits in a number
# time complexity: O(log n), n = the input number itself, not the length of number


def sumDigits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


