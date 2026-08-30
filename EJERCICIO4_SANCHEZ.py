contador = 0
suma = 0
for i in range(1,21):
    if i % 2 ==0:
        contador = contador + 1
        suma = suma + i
print(f"La cantidad de pares es {contador}")
print(f"La suma de los numeros oares es {suma}")