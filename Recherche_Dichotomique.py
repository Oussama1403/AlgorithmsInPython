#Oussama

def Remplire():
    n = int(input("Saisire la taille du tableau :"))
    T = []
    for i in range(n):
        T.append(int(input("Saisire T[{0}] :".format(i))))
    T = sorted(T)
    x = int(input("Saisire le nombre :"))
    return T,n,x

def Rechdicho(T,n,x):
    
    Binf = 0
    Bsup = n - 1
    mid = 0    
    while Binf <= Bsup:     
    	mid = (Bsup + Binf) // 2    
    	if T[mid] < x: 
    		Binf = mid + 1    
    	elif T[mid] > x: 
    		Bsup = mid - 1    
    	else: 
    		return True 
    return False

T,n,x = Remplire()
r = Rechdicho(T,n,x)
print(r) 
