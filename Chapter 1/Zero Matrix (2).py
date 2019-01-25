'''
Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to 0.
This implementation is more space efficient than the 1st one.
'''


def makeRowZero(m, row):
    for i in range(len(m[0])):
        m[row][i] = 0


def makeColZero(m, col):
    for i in range(len(m)):
        m[i][col] = 0


def printMatrix(m):
    for r in m:
        for n in r:
            print(n, ' ', end='')
        print()


def ZeroMatrix2(m):
    fstRowZero, fstColZero = False, False
    w, h = len(m[0]), len(m)
    if h == 0:
        return

    for i in range(w):
        if m[0][i] == 0:
            fstRowZero = True
            break
    for i in range(h):
        if m[i][0] == 0:
            fstColZero = True
            break

    for i in range(1, h):
        for j in range(1, w):
            if m[i][j] == 0:
                m[i][0] == 0
                m[0][j] == 0

    for i in range(1, h):
        if m[i][0] == 0:
            makeRowZero(m, i)
    for i in range(1, w):
        if m[0][i] == 0:
            makeColZero(m, i)

    if fstRowZero:
        makeRowZero(m, 0)
    if fstColZero:
        makeColZero(m, 0)

    return m


