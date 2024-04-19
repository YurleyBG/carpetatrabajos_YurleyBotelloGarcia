precio=int(50)#precio de la suscripcion
account=int(input("ingrese el valor de su cuenta actual: ")) #valor de la cuenta
#menu de opciones presentadas al usuario
print(":::::::::::PYTIMEsUSER::::::::::::::::::::::::")
print("el valor de cada suscripcion es de: 50")
print("===================MENU=======================")
print("1. comprar un suscripcion")
print("2. regalar suscripcion")
print("3. revisar el dinero de su cuenta")
print("4. recargar cuenta")
print("5. finalizar")
print("==============================================")


bool=True
while bool:#ciclo while
   opc=int(input("\ningrese su opcion, por favor : "))#permite elegir una  opcion

   if opc==1:#primera opcioncompra de suscripciones
      print("------COMPRAR SUSCRIPCIONES-------")

      if account>=precio:#verifica si el dinero del cliente es mayor al de el valor de la suscripcion sie asi hara el siguiente proceso
         
         print("recuerda estas suscripciones son anuales:  ")
         name=input("\ningrese su nombre: ")#pide al usuario su nombre
         
         susc=int(input("\ningrese cuantas suscriciones desea: "))#pide al ususrio la cantidad que desea
         
         print("\na que año desea agregar su suscripcion entre(1990 y2020) : ")#pide agregar los años o año
         year=input()#permite al usuario escribirlos
          
         multi=precio*susc#se multiplica la cantidad de suscriciones por el precio
         saldo=account- multi#se le resta al dinero del usuario la cantidad anterior
         account=saldo#cambia al nuevo saldo del usuario

         print("esta suscripcion corresponde a:",name, "por una cantidad anual de :",susc,"año "
            "que corresponde a el siguiente año:", year,)#da como respuesta de quien fue la suscripcion a que año y cuantas
         print("Su sucripcion fue Exitosa!!")#mensaje que verifica la suscripcion
      else:   
         print("su dinero no es suficiente para hacer esta suscripcion recargue")#si el dinero del usuario es menor al precio mandara este mensaje
            
       
   elif opc==2:#opcion 2 del menu
      
      print("=======REGALAR SUSCRIPCIONES===========")

      if account>=precio:#verifica si el dinero del cliente es mayor al de el valor de la suscripcion sie asi hara el siguiente proceso
         cant=int(input("cuantas suscripciones desea regalar: "))#le pregunta al usuario cuantas suscripciones desea regalar
         for i in range(cant): #dependiendo de la cantidad imprimira en un ciclo
          nom=input("\ningrese el nombre: ")#pidira ingresar el nombre del ususario a regalar
          years=int(input("\ningrese el año en que quiere regalar la suscripcion: "))#pregunta al año que quiere regalarle
          print("Su sucripcion regalo fue Exitosa!!")#dice que la suscripcion a regalar fue exitosa
          print("esta suscripcion corresponde a:",nom,"que corresponde al  siguiente año:", years,)#muestras los datos
      
         can=precio*cant#se multiplica la cantidad de suscriciones por el precio
         diner=account-can#se le resta al dinero del usuario la cantidad anterior
         account=diner#cambia al nuevo saldo del usuario
      else:
          print("su dinero no es suficiente para hacer esta suscripcion recargue")#si el dinero del usuario es menor al precio mandara este mensaje
          
 
   elif opc==3:#opcion 3
       print("\nesta es su cuenta actual:",account,)#muestra el saldo total del usuario
       
   elif opc==4:#opcion 4
       print("========RECARGAR============")

       print("\ncuanto dinero desea agregar a su cuenta")#pregunta al ususario cuanto dinero desea recargar
       newmoney=int(input())#le permite al usuario escribirlo
       account=account+newmoney#le suma el nuevo dinero agregado a la cuenta del usuario
      
   elif opc==5:#opcion 5
      print("\nusted a finalizado este programa, bye ;)") #finaliza todo el programa y lo despide
      break #rompe ele bucle
bool=False #cierra todo
#desarrollado por yurley botello TI:1066085539