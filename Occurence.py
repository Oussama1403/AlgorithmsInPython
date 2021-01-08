def Saisir():
   ok = False
   while not ok or n<5:
      n = int(input("Saisir la taille du tableau :"))
      ok = True
   
   T = []
   for i in range(n):
      print("Saisire T[",i,"] :")
      x = input()
      while not all(chr.isalpha() or chr.isspace() for chr in x):
         print("Saisire T[",i,"] :")
         x = input()
      T.append(x)   
   
   return T,n    

def Occurence(T,n):
   V = []
   for elem in T:
      c = elem.count(' ')
      V.append(c)
   return V      


T,n = Saisir()
print(T)
V = Occurence(T,n)
print(V)




