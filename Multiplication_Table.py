#Create a multiplication table using two dimensional list in python.

def Creation():
    n = 10
    M = [0]*n
    for i in range(n):
        M[i] = [0]*n
    n1 = 0
    n2 = 0
    for i in range(n):
        n1 = i + 1
        for j in range(n):
            n2 = j + 1
            M[i][j] = n1 * n2  
    return n,M

def PrintList(n,M):
    for i in range(n):
        print()
        for j in range(len(M[i])):
            print(M[i][j],end="|")

n,M = Creation()
PrintList(n,M)