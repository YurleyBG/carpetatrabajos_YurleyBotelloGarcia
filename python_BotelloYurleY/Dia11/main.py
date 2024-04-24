import json#importamos json
file="large-file.json"#colocamos el nombre de nuestro archivo json  en una variable

with open( file, encoding="utf-8") as info:
            dato= json.load(info)#con esto lo convertimos a python
#nuestro menu de opciones
print("===================MENU==========================")
print( "1.  acceder a tipos de eventos")
print( "2.  Crear")
print( "3.  Eliminar")
print( "4.  Actualizar")
print( "5.  revisar")
print( "6.  salir")
print( "================================================")

bool=True
while bool:
        opc=int(input("ingrese una opcion por favor : "))

        if opc==1:
                print("=================Nuestros Eventos==============")
                event=[]#guarda los nombres de los eventos 
                for i in range(len(dato)):#permite ir por cada uno
                 if dato[i]["type"] not in event:#si el nombre no se encuentra en la lista
                   event.append(dato[i]["type"])#con esto procedera aa garegarlo
        
                e=json.dumps(event,indent=1)#nos permite verlo mas ordenado
                print(e)#imprime
                print("================================================")

        elif opc==2:
              print("===============Añadir=================")
              #permite tener los nombres de los eventos
              evento=[]
              for i in range(len(dato)):
                 if dato[i]["type"] not in evento:
                   evento.append(dato[i]["type"])
              #el usuario ingresa el nuevo nombre del evento que desea
              opceven=input("ingrese el nombre del nuevo evento a añadir: ")
              if opceven not in evento:# si no esta en la lista anterior
                    evento.append(opceven)#con esto no lo ingresara a la lista
                    print(evento)#imprime
              print("================================================")
              
        elif opc==3:#no funciona
                print("===============Eliminar=================")  
                eventi=[]
                for i in range(len(dato)):
                 if dato[i]["type"] not in eventi:
                   eventi.append(dato[i]["type"])
                   

                elieven= input("ingrese el nombre del evento que desea eliminar : ")
                if elieven==eventi:
                 eventi.remove(elieven)
                 print(eventi)
                elif elieven not in eventi:
                 print("este nombre de evento no se encuentra")
                continue

                
        

                
                print("================================================")

        elif opc==4:
                print("===============Actualizar=================")
                print("================================================")
        elif opc==5:
                print("===============Revisar=================")
                print("================================================")
        elif opc==6:#se despide del usuario
                 print(" ")
                 print("===============Salir=================")
                 print("")
                 print("Usted a decidido abandonar este programa")
                 print("           HASTA LA PROXIMA ;)          ")
                 print("          ······GOODBYE·······          ")
                 print("================================================")
                 break

bool=False
              
        
#desarrollado por yurley botello T.I 1066085539