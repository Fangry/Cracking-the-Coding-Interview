'''
Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to 0.
'''


def ZeroMatrix1(m):
    w, h = len(m[0]), len(m)
    if h == 0:
        return
    zeroRow, zeroCol = [1 for i in range(h)], [1 for i in range(w)]
    for i in range(h):
        for j in range(w):
            if m[i][j] == 0:
                zeroRow[i] = 0
                zeroCol[j] = 0

    for i in range(w):
        if zeroCol[i] == 0:
            for j in range(h):
                m[j][i] = 0

    for i in range(h):
        if zeroRow[i] == 0:
            for j in range(w):
                m[i][j] = 0

    return m


def printMatrix(m):
    for r in m:
        for n in r:
            print(n, ' ', end='')
        print()
