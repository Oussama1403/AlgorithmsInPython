from math import sqrt
print("Bienvenue,\nCe programme développé par Oussama Ben Sassi vous aidera à résoudre les équations du deuxième degré.")

while True:
    try:
        print("Une equation du deuxième degré est sur la form ax²+bx+c=0 ou a ,b ,c sont des réels avec a≠0")
        print('--------------------------------------------------------------------------------------------')
        a = int(input("Entrer a :"))
        b = int(input("Entrer b :"))
        c = int(input("Enter c :"))
      
        #calculer le discriminant:
        if a == 0:
            print("'a' doit être différent de 0")
            break
        
        print(f"Calculer le discriminant {b}²-4*{a}*{c}")
        delta = b**2 - 4 * a * c
        
        if delta < 0:
            print(f"le discriminant de {a}x²+{b}x+{c} est {delta}\n{delta} < 0")
            print(f"l'équation {a}x²+{b}x+{c} n'a pas de solution réelle.")
            break
        elif delta == 0:
            print(f"le discriminant de {a}x²+{b}x+{c} est {delta}\n{delta} = 0")
            x = -b / 2 * a
            print(f"l'équation {a}x²+{b}x+{c} a une seul solution: [x = {x}]")
            break
        else :
            print(f"le discriminant de {a}x²+{b}x+{c} est {delta}\n{delta} > 0")
            x_prime = ( (-b) + sqrt(delta) ) / (2 * a) 
            x_seconde = ( (-b) - sqrt(delta) ) / (2 * a)
            print(f"l'équation {a}x²+{b}x+{c} a deux solutions distinctes: [x1 = {x_prime} , x2 = {x_seconde}]")
            break 
    except :
        print("Une erreur s'est produite")
        break    



 

