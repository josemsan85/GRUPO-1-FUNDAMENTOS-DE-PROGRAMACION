

numero = int (input ("Ingrese numero N " ))

for a in range (2, numero+1):

    raiz = int (a ** 0.5)

    if raiz*raiz == a:
        print(str(a))

    esprimo = True

    for b in range (2, a):

        if a % b == 0:

            esprimo = False; 
            break

    if esprimo == True:

        print("el numero primo es " +  str(a)) 

