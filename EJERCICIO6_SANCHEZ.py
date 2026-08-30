#Numeros Primos hasta N
import math
N = int(input("Ingrese un numero: "))
for numero in range (2,N+1):
    es_primo = True 
    for divisor in range(2, int(math.sqrt(numero)) + 1):
        if numero % divisor == 0:
            es_primo = False 
    if es_primo == True:
        print(f"El numero {numero} es primo")