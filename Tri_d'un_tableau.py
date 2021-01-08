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
    for i in range(len(T)):
        for j in range(i+1,len(T)):
            if T[j] < T[i]:
                num1 = T[i]
                num2 = T[j]
                T[i] = num2
                T[j] = num1
    return T

n = Saisir()
T = Remplir(n)
print(T)
l = Trisel(T,n)
print(l)



