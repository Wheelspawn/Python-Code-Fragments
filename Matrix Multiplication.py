import random

# these methods will modify your data. Make copies if you want to save your original variables

def randomMatrix(n, m, r1, r2): # generates matrix of random ints in specified range
    x = []

    for i in range(n):
        x.append([])
        for j in range(m):
            x[i].append(random.randrange(r1, r2))
    return x

def zeroMatrix(n,m): # generates a matrix filled with zeroes
    x = []
    for i in range(n):
        x.append([])
        for j in range(m):
            x[i].append(0)
    return x

def matrixMultiplication(n, m): # multiplies two matrices together
    ops = 0
    x = []

    for i in range(len(n)):
        x.append([])
        for j in range(len(m[i])):
            x[i].append(0)

    for i in range(len(x)):
        for j in range(len(x[0])):
            for k in range(len(n[0])):
                x[i][j] += n[i][k] * m[k][j]
                ops += 1
    print("Multiplication operations: ", ops)
    return x

def matrixAddition(a, b): # adds matrix a into matrix b
    if len(a) != len(b):
        print("matrices are not of the same size")
    else:
        for i in range(len(a)):
            if len(a[i]) == len(b[i]):
                for j in range(len(a[i])):
                    b[i][j] += a[i][j]
            else:
                print("matrices are not of the same size")

def rowAddition(a, i, j): # adds row i into row j
    for k in range(len(a[i])):
        a[j][k] += a[i][j]
    
def rowMultiplication(a, i, m): # multiplies row i by m
    for k in range(len(a[i])):
        a[i][k] = a[i][k]*m

def scalarMultiplication(a, s): # multiplies matrix a by s
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = a[i][j] * s

def scalarDivision(a, s): # divides matrix a by s
    scalarMultiplication(a, 1/s)

def rowDivision(a, i, d):
    rowMultiplication(a, i, 1/d)
