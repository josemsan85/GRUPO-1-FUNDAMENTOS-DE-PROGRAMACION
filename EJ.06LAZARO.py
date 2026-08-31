#Numeros Primos hasta N
n = int(input("Escribe un numero N: "))

for numero in range(2, n + 1):
    es_primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, "es primo")
