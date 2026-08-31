#Calculadora Basica (4 operaciones)
n1 = float(input("Escribe el primer numero: "))
n2 = float(input("Escribe el segundo numero: "))
operador = input("Escribe el operador (+, -, *, /): ")

match operador:
    case "+":
        resultado = n1 + n2
        print("Resultado:", resultado)
    case "-":
        resultado = n1 - n2
        print("Resultado:", resultado)
    case "*":
        resultado = n1 * n2
        print("Resultado:", resultado)
    case "/":
        if n2 == 0:
            print("Error: no se puede dividir entre cero")
        else:
            resultado = n1 / n2
            print("Resultado:", resultado)
    case _:
        print("Operador no valido")