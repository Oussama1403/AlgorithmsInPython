#Méthode de Tri à bulle.

def Saisir():
   ok = False
   while not ok or n<5 or n>20:
      n = int(input("Saisir la taille du tableau :"))
      ok = True
   return n

def Remplir(n):
    T = []
    for i in range(n):
        m = int(input("Saisir les entiers de la tableau :"))
        while m<0:
            m = int(input("Réssayer avec un nombre positive,Saisir les entiers de la tableau :"))
        T.append(m)       
    return T       

def Trisel(T,n):
    #Parcourir le tableau et réduise sa taille de 1
    for parc in range(n-1,0,-1):
        for i in range(parc):
            #print("i",T[i])
            if T[i+1] < T[i]:
                T[i+1],T[i] = T[i],T[i+1]
            #print(T)      
    return T

n = Saisir()
T = Remplir(n)
print(T)
l = Trisel(T,n)
print(l)



