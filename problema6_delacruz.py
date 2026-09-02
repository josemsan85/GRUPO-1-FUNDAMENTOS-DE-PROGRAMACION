# Números primos hasta N

n = int(input("Ingrese un número: "))

for numero in range(2, n + 1):
    primo = True
    for i in range(2, numero):
        if i ** 2 > numero:
            break

        if numero % i == 0:
            primo = False
            break

    if primo:
        print(numero)