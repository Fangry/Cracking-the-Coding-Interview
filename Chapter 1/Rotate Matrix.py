'''
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''


def makeMatrix(n):
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(j+1+n*i)
    return m


def printMatrix(m):
    for r in m:
        for n in r:
            print(n, ' ', end='')
        print()


def rotateMatrix(m):
    n = len(m)
    if len(m) == 0 or len(m) != len(m[0]):
        print('error with matrix')

    for layer in range(int(n/2)):
        fir, las = layer, n - layer - 1
        for i in range(fir, las):
            offset = i - fir
            top = m[fir][i]
            m[fir][i] = m[las-offset][fir]
            m[las-offset][fir] = m[las][las-offset]
            m[las][las-offset] = m[i][las]
            m[i][las] = top
    return m


m = makeMatrix(4)
printMatrix(m)
print()
rm = rotateMatrix(m)
printMatrix(rm)
