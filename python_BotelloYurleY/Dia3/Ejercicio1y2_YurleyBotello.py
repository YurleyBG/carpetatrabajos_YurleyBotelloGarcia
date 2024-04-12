#1. Crear una función que determina si un número dado por el usuario es primo. Un número primo es aquel que solo 
# es divisible por 1 y por sí mismo. El programa proporciona un menú interactivo que permite al usuario ingresar números 
#para ser verificados como primos. Además, se incluye la opción de detener el proceso cuando el usuario lo desee.
#Al inicio, el programa dará la bienvenida y explicará el propósito del aplicativo: verificar si un número dado es primo o no.
#Se presentará un menú con opciones numeradas para que el usuario pueda elegir entre verificar un número, detener el programa u obtener información adicional.
#Si elige verificar un número, se le solicitará ingresar el número deseado.
#La función verificará si el número es primo y proporcionará un mensaje claro indicando el resultado.
#Después de cada verificación, se volverá al menú para permitir al usuario realizar más acciones.
#Si elige detener el programa, se le despedirá y el programa se cerrará.
#Si elige obtener información adicional debe arrojar una explicación de los números primos y el nombre del autor del aplicativo.


#da la bienvenida al ususrio a programita de verificar numeros primos.

print(".............................................")
print("________BIENVENIDO A NUESTRO PROGRAMA________")
print(".............................................")

print("Estas preparado, iniciaremos mostrandote el menu de nuestro programita")
print(" !!LISTO!! vamos allà")


print("  ")

print("Este es nuestro menu elige una opcion")
print("")

#nuestro menu  de opciones para el usuario

print("________________________MENU DE OPCIONES______________________")
print("1. Verificar de numeros primos ")
print("2. Informacion extra ")
print("3. Finalizar programa ")
print("__________________________________________________________________")


retri=True #condicion como verdadera
while retri:   #utilizaremos un el bucle while para almacenar todo el proceso que se iran repitiendo segun la condiciom dada
    opc=int(input("Ingrese su opcion porfavor: "))#le pide al usuario que ingrese el numer
    print(" ")#espacio
    if opc==1:#dirige a la opcion 1 del menu, donde se verificara si tal numero es primo o no
        print( "__VERIFICADOR DE NUMEROS__") #nombre de la opcion 
        print(" ")

        num=int(input("Ingrese un valor numerico porfavor: "))#permite al usuario ingresar su numero
        print(" ")
        n=int(2)#le da un valor en este caso 2 a la variable n
        nu=num%n#el valor anterior se divide con el numero ingresado por el usuario

        if nu==0:
            print("Este numero no es primo") #indica que el numero no es prim
        
        else:
            print(f"Este numero es primo: {num}") #nos indica que el numero es primo
            continue#continua con el programa
    elif opc==2:#muestra informacion adicional si el usuario lo desea

        print("___BIENVENIDO A A LA SECION DE INFORMACION___")    
        print(" ")  
        print(" -NUMEROS PRIMOS-")  
        print("Los números primos son aquellos que solo son divisibles por ellos mismos. Si se intenta dividir ")
        print("por otro número nunca dará una cifra exacta salvo que se divida por 1 o por sí mismo.")
        print("")
        print("___EJEMPLOS DE NUMEROS PRIMOS___")
        print("3,5,7,11,13,17,19,23,29,31...")
        print(" ")
        print("ESTE PROGRAMA FUE DESARROLLADO POR: Yurley Botello Garcia.")
        print(" ")
        print(" ")
    elif opc==3:#permite al usuario abandonar el programa

      print( "usted a finalizado con el programa")
      print(" ")
      print("________HASTA LA PROXIMA__________")
      print("adioos!!! ;)")
      break #cierra el programa
retri=False#condicion como falsa,termina el programa

print ("")
print ("")
print ("")
#2. Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y 
#decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos. La generación de contraseñas se
#realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve una contraseña segura. 
#El programa ofrece un menú interactivo para probar el generador de contraseñas y permite al usuario realizar múltiples 
#solicitudes.
#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
#Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.
#Utilizará una función para generar la contraseña según las preferencias del usuario.
#Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.
#Si el usuario decide salir, se despedirá y el programa se cerrará.
#Se manejarán casos de entrada no válida, como letras en lugar de números para la longitud de la contraseña.


print("----------------------------------------------------")
print("..............BIENVENIDO A PROGRAMITA...............")
print(".............(Generador de Contraseña)..............")
print("----------------------------------------------------")
print(" ")
print(" nuestro generador de contraseña es seguro y  tiene  facilidad de eleccion")
print("Quieres unirte a esta experiencia, les't goo!!")
print(" ")

print("________________________MENU DE OPCIONES______________________")
print("1. elegir longitud de la contraseña ")
print("2. incluir mayusculas")
print("3. incluir minusculas")
print("4. incluir caracteres numericos y simbolos")
print("5.generar contraseña")
print("6. salir")
print("__________________________________________________________________")
print(" ")

#import random

          

#lon=True
#while lon :
    #opci=int(input("ingrese su  opcion"))

    #if opci==1:
        
       # print("cantidad de digitos en su contraseña")
    #dig=int(input("ingrese la cantidad de digitos que quiere para su contraseña"))
    #print(" ")  
    #if opci==2:
      # print("letras minusculas")
       # minuscu="abcdefghijklmnopqrstuvwxyz"
        #minu=int(input("desea agreagar letras minusculas "))
       # if minu=="si":
       #   min=int(input("cuales  desea agregar"))
       # else:
           # print("no desea ninguna")
           # break
            
   # elif opci==3:
        #print("letras mayusculas")
       # mayus=minuscu.upper()
       # mayu=int(input("desea agreagar letras mayusculas "))
       # if mayu=="si":
          #may=int(input("cualesdesea agregar"))
       # else:
            #print("no desea ninguna")
            #break
            
            
     #elif opci==4:
         #print("numeros y simbolos")
        # nume = "0123456789"
        # simb = "{}[]()*;/,_-"
        #sib=input("desea agregar simblos")
         #num=int(input("desea agreagar numeros "))
         #if num=="si":
           #nu=int(input("cuales desea agregar"))
         #else:
            # print("no desea ninguna")
            
         #if sib=="si":
            #sib=input("cuales desea agregar")
           # break
         #elif opci==5:
            #minusc=min
            #mayus=may
            #nume = nu
            #simb =sib

            #contra = minusc+mayus+nume+simb
           # longitud=dig

           # contra_r=random.sample(contra, longitud)
          # passworde=" ".join(contra)
          # print(passworde)

        #elif opci==5:
        # print("haz abandonado el programa")
       # print("HASTA LA PROXIMA")
        #break
  
#lon=False

import random

def pass_ge(longi):

    minusc="abcdefghijklmnopqrstuvwxyz"
    #minu=str(input("que letras quiere agregar"))
    mayuscu=minusc.upper()
   # mayus=str(input("que letras quiere agregar"))
    num="0123456789"
    #n=int(input("que numero quiere agregar"))
    sim="{}[]()*;/,_-"
    #sib=input("que simbolos quiere agregar")

    longit=int(input("ingrese la cantidad de digito que desea que tenga su contraseña : "))

    result= minusc + mayuscu + num+ sim
    longi=longit
    passworu=random.sample(result, longi)

    passwor_r = "".join(passworu)

    return passwor_r

contrase=pass_ge("long")
print("password," , {contrase})





#desarrollado por Garcia Botello Yurley  T.T 1066085539