#Contar y Sumar Pares del 1 al 20
contador = 0
suma = 0

for i in range(1, 21):
    if i % 2 == 0:
        contador = contador + 1
        suma = suma + i

print("Cantidad de números pares:", contador)
print("Suma de los números pares:", suma)