#aca se coloca las notas de cada uno de los alumnos 
numero = [12, 20, 14, 11, 16]

#de manera preliminar se asigna el primer elemento del array a una variable de nombre mayor
mayor = numero[0]

#de manera preliminar se asigna el primer elemento del array a una variable de nombre menor
menor = numero[0]

#alumnos que hasta el momento han aprovado
alumnosAprovados = 0 

for i in numero :
# 12 20 14 11 16
# si alguna nota es mayor a 20 o menor a 0. Se rompe el bucle
    if i < 0 or i > 20:
      print("Coloca una nota entre 0 y 20")
      break 
    
# el i representa a cada elemento del array
# si es mayor a 11 entonces la cantidad de alumnos aprovados se eleva a uno 
    if  i >= 11:
        alumnosAprovados += 1

    #si cada elemento del array es mayor a la variable asignada 
    #entonces se le asigna a la variable mayor, si no lo es entonces 
    #mantiene su valor 
    if ( i > mayor):

        mayor = i

    #si cada elemento del array es menor a la variable asignada 
    #entonces se le asigna a la variable menor, si no lo es entonces 
    #mantiene su valor 
    if (i < menor):

        menor = i

    # se espera a que sea el ultimo numero del bucle for para mostrar los resultados
    # mayor menor y alumnos aprovados 

    if (i == numero[len(numero)-1]):

        #esta linea calcula el promedio de notas la suma de notas sobre el total de notas 
        #sum numero es igual a la suma de los elementos del array y len numero es igual a la cantidad de elementos
        #del array

        print ("el promedio es " + str ( sum(numero)/len(numero) ))

        print ("el numero menor es " + str(menor))
        print ("el numero mayor es " + str(mayor))
        print ("la cantidad de alumnos aprovados es " + str(alumnosAprovados))




