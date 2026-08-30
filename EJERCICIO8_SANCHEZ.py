#Promedio y estadisticas
N = int(input("Ingrese el numero de estudiantes: "))
suma = 0
aprobados = 0
for i in range (N):
    nota = float(input("Ingrese la nota del estudiante: "))
    suma = suma + nota 
    if i == 0:
        mayor = nota
        menor = nota
    else:
        if nota > mayor:
            mayor = nota
        if nota < menor:
            menor = nota
    if nota >= 11:
        aprobados = aprobados +1
promedio = suma / N
print(f"El promedio de los estudiantes fue: {promedio:.2f}")
print(f"La nota mas alta fue: {mayor}")
print(f"La nota mas baja fue: {menor}")
print(f"La cantidad de estudiantes aprovados fue: {aprobados}")