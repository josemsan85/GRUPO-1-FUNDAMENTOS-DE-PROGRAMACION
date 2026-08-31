import random

#Adivina el Numero (Do-While)
secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el numero (1-100): "))
    intentos = intentos + 1

    if intento == secreto:
        print("Correcto Adivinaste en", intentos, "intentos")
        break
    elif intento < secreto:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")