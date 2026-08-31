#Promedio y Estadisticas
n = int(input("Cuantos estudiantes son: "))

notas = []

for i in range(n):
    nota = float(input("Escribe la nota: "))
    notas.append(nota)

suma = sum(notas)
promedio = suma / n
nota_maxima = max(notas)
nota_minima = min(notas)

aprobados = 0
for nota in notas:
    if nota >= 11:
        aprobados = aprobados + 1

print("Promedio:", promedio)
print("Nota mas alta:", nota_maxima)
print("Nota mas baja:", nota_minima)
print("Estudiantes aprobados:", aprobados)