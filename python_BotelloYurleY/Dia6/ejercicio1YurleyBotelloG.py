num2=[]#nueva lista donde no estaran los numeros repetidos.

for i in range(0,300): #utilizamos un bucle for para iniciar un ciclo con un limite de 300 veces
   
   num1=int(input())#le permite al usuario agregar los numeros a la lista 1

   if num1 not in num2:#verifica si el los numeros de la lista 1 no esta en la lista 2

    num2.append(num1)#si el numero no esta con el append se ingresara al final de la lista
    num2.sort()#el sort es utilizado para ordenar los valores de una lista de manera ascendentes
    print(num2)#imprimimos los datos de la lista 2 para que se muestren en la terminal
    
   elif -100<=num2 <=100:#nos permite ordenar los numero que pasan del 10 de manera correcta.
     print(num2)#imprimimos 

#Desarrollado por Garcia Botello Yurley T.T 1066085539