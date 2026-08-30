#Adivina el numero
import random
numero_aleatorio = random.randint(1,100)
intento = int(input("Intenta adivinar el numero secreto: "))
intentos = 1
while intento != numero_aleatorio:
    if intento > numero_aleatorio:
        print("El numero secreto es menor")
    elif intento < numero_aleatorio:
        print("El numero secreto es mayor ")
    intento = int(input("Sigue intentando: "))
    intentos = intentos + 1
print("Has acertado, felicidades!!!")
print(f"Intentos : {intentos} ")
if intentos < 5:
    print("Eres lo maximo")
else:
    print ("Aun se puede mejorar, suerte a la proxima") 