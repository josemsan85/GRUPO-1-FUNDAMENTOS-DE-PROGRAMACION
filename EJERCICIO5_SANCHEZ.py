#Calculadora basica
num1 = float(input("Escriba el primer numero: "))
num2 = float(input("Escriba el segundo numero: "))
ejercicio = input("Escriba el ejercicio a realizar: ")
match ejercicio:
    case "+":
        print(f"La suma es: {num1 + num2} ")
    case "-":
        print(f"La resta es: {num1 - num2}")
    case "*":
        print(f"El resultado de la multiplicacion es: {num1 * num2}")
    case "/":
        if num2 == 0:
            print("No se puede dividir entre 0")
        else:
            print(f"El resultado de la division es {num1 / num2}")