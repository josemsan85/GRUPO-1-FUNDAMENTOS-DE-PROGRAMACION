import random
intentos = 0 
while True:

 numero = int (input ("Adivina el numero "))
 aleatorio = random.randint(1,100) 

 if numero == aleatorio :

    print ("has acertado el numero aleatorio " + str(numero) )
    print ("Tu numero de intentos fue " + str(intentos))
    break 

 elif numero < aleatorio:
    print ("tu numero elegido " + str(numero) + " elegido es menor al aleatorio " + str(aleatorio))
    intentos +=1 

 elif numero > aleatorio:
    print ("tu numero elegido" + str(numero) + " elegido es mayor al aleatorio " + str(aleatorio))
    intentos +=1

 print(str(aleatorio))