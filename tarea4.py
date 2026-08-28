
contador  = 0 
sumaPares = 0 

for i in range (1,21):
    if i % 2 == 0:
        contador +=1
        sumaPares += i

    if i == 20:
        print ("La cantidad de pares es " + str (contador))
        print ("la suma de pares es " + str (sumaPares))
