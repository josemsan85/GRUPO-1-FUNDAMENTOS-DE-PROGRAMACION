import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    numero = int(input("Adivina el número (1-100): "))
    intentos += 1
    
    if numero < numero_secreto:
        print("El número secreto es mayor")
    elif numero > numero_secreto:
        print("El número secreto es menor")
    else:
        print("¡Correcto!")
        print("Intentos:", intentos)
        break