
num1 = int (input ("El primer  numero "))
num2 = int (input ("El segundo numero ")) 

operador = input ("Elige tu operador ")
if operador == "/" and num2 == 0: 
 
 print ("esta operacion no se puede hacer")

else :
 match operador:

    case  "+":
        print ("La suma es " + str( num2+ num1 ))

    case "-":
        print ("La resta es " + str( num1 - num2))

    case "*":
        print ("La multiplicacion es " + str( num1 * num2))

    case "/":
        print ("La division es " + str( num1 / num2))

