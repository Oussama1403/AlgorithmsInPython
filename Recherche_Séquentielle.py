#Program pour démonstrer le Méthode de Recherche Séquentielle

def Remplire():
    n = int(input("Saisire la taille du tableau :"))
    T = []
    for i in range(n):
        e = int(input("Saisire T[{0}] :".format(i)))
        T.append(e)
    return T

def Recherche_Séc(T):
    n = int(input("Entrer le nombre Pour le rechercher dans le tableau :"))
    for i in range(len(T)):
        if T[i] == n:
           x = True
           break
        else:
           x = False
    return x                
                
T = Remplire()
print(T)
B = Recherche_Séc(T)
print(B)
