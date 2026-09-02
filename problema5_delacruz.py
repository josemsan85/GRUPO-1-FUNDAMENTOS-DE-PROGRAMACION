# Calculadora básica
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operador == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operador == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("No se puede dividir entre cero")
else:
    print("Operador no válido")