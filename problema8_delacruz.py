# Promedio y estadísticas

n = int(input("¿Cuántas notas va a ingresar? "))
suma = 0
aprobados = 0

for i in range(1, n + 1):
    nota = float(input(f"Ingrese la nota {i}: "))
    suma += nota

    if nota >= 11:
        aprobados += 1

    if i == 1:
        mayor = nota
        menor = nota
    else:
        if nota > mayor:
            mayor = nota

        if nota < menor:
            menor = nota

promedio = suma / n
print("Promedio:", promedio)
print("Nota más alta:", mayor)
print("Nota más baja:", menor)
print("Cantidad de aprobados:", aprobados)