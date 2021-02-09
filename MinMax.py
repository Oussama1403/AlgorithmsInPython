import random

def Remplissage():
    ok = False
    while not ok or l<3 or l > 10:
        l = int(input("Entrer le nombre de lignes :"))
        ok = True
    ok = False    
    while not ok or c<4 or c>12:
        c = int(input("Entrer le nombre de colonnes :"))
        ok = True
    M = []
    for i in range(l):
        M.append([0]*c)        
    
    for i in range(l):
        for j in range(c):
            M[i][j] = random.randint(1,100)
    print(M)
    return l,c,M        

def Min(l,c,M):
    min = M[0][0]
    for i in range(l):
        for j in range(c-1):
            #print(min)
            if M[i][j] < min:
                min = M[i][j]
    return min                

def Max(l,c,M):
    max = M[0][0]
    for i in range(l):
        for j in range(c-1):
            #print(max)
            if M[i][j] > max:
                max = M[i][j]
    return max   


l,c,M = Remplissage()

min = Min(l,c,M)
print("le minimum de la matrice est :",min)
max = Max(l,c,M)
print("le maximum de la matrice est :",max)