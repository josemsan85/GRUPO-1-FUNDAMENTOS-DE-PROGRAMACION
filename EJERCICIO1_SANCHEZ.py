#Calculo del area y perimetro de un rectangulo

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
area = base * altura
print(f"El area del rectangulo es: {area:.2f}")
perimetro = 2*(altura + base)
print(f"El perimetro del rectangulo es: {perimetro:.2f}")
