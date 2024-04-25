#!/usr/bin/python
# -- coding: utf-8 --
import json
file="large-file.json"

with open(file, encoding="utf-8") as openfile:
    miJSON= json.load(openfile)
 
crearEventos=[]#guarda los datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])




for q in range (1470):
    print("========================")
    print(":::: Evento # ",q+1,"::::")
    print("========================")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])
    print("------- login:",crearEventos[q]['actor']['login'])
    print("------- avatar:",crearEventos[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",crearEventos[q]['repo']['id'])
    print("-----------name:",crearEventos[q]['repo']['name'])
    print("----------------public:",crearEventos[q]['public'])
print("================================================")
print("")

eventoempuje=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='PushEvent'):
        eventoempuje.append(miJSON[i])


for q in range (5814):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventoempuje[q]['id'])
    print("Tipo:",eventoempuje[q]['type'])
    print("Actor:")
    print("------- ID:",eventoempuje[q]['actor']['id'])
    print("------- login:",eventoempuje[q]['actor']['login'])
    print("------- avatar:",eventoempuje[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventoempuje[q]['repo']['id'])
    print("-----------name:",eventoempuje[q]['repo']['name'])
    print("----------------public:",eventoempuje[q]['public'])
print("================================================")
print("")

verevento=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='WatchEvent'):
        verevento.append(miJSON[i])


for q in range (1229):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",verevento[q]['id'])
    print("Tipo:",verevento[q]['type'])
    print("Actor:")
    print("------- ID:",verevento[q]['actor']['id'])
    print("------- login:",verevento[q]['actor']['login'])
    print("------- avatar:",verevento[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",verevento[q]['repo']['id'])
    print("-----------name:",verevento[q]['repo']['name'])
    print("----------------public:",verevento[q]['public'])
print("================================================")
print("")

eventolanzamiento=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='ReleaseEvent'):
        eventolanzamiento.append(miJSON[i])


for q in range (59):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventolanzamiento[q]['id'])
    print("Tipo:",eventolanzamiento[q]['type'])
    print("Actor:")
    print("------- ID:",eventolanzamiento[q]['actor']['id'])
    print("------- login:",eventolanzamiento[q]['actor']['login'])
    print("------- avatar:",eventolanzamiento[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventolanzamiento[q]['repo']['id'])
    print("-----------name:",eventolanzamiento[q]['repo']['name'])
    print("----------------public:",eventolanzamiento[q]['public'])
print("================================================")
print("")
eventosolicitudextraccion=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='PullRequestEvent'):
        eventosolicitudextraccion.append(miJSON[i])


for q in range (473):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventosolicitudextraccion[q]['id'])
    print("Tipo:",eventosolicitudextraccion[q]['type'])
    print("Actor:")
    print("------- ID:",eventosolicitudextraccion[q]['actor']['id'])
    print("------- login:",eventosolicitudextraccion[q]['actor']['login'])
    print("------- avatar:",crearEventos[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventosolicitudextraccion[q]['repo']['id'])
    print("-----------name:",eventosolicitudextraccion[q]['repo']['name'])
    print("----------------public:",eventosolicitudextraccion[q]['public'])
print("================================================")
print("")

eventoasunto=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='IssuesEvent'):
        eventoasunto.append(miJSON[i])


for q in range (544):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventoasunto[q]['id'])
    print("Tipo:",eventoasunto[q]['type'])
    print("Actor:")
    print("------- ID:",eventoasunto[q]['actor']['id'])
    print("------- login:",eventoasunto[q]['actor']['login'])
    print("------- avatar:",eventoasunto[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventoasunto[q]['repo']['id'])
    print("-----------name:",eventoasunto[q]['repo']['name'])
    print("----------------public:",eventoasunto[q]['public'])
print("================================================")
print("")

eventotenedor=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='ForkEvent'):
        eventotenedor.append(miJSON[i])

      
for q in range (354):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventotenedor[q]['id'])
    print("Tipo:",eventotenedor[q]['type'])
    print("Actor:")
    print("------- ID:",eventotenedor[q]['actor']['id'])
    print("------- login:",eventotenedor[q]['actor']['login'])
    print("------- avatar:",eventotenedor[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventotenedor[q]['repo']['id'])
    print("-----------name:",eventotenedor[q]['repo']['name'])
    print("----------------public:",eventotenedor[q]['public'])
print("================================================")
print("")

eventogollum=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='GollumEvent'):
        eventogollum.append(miJSON[i])



for q in range (60):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventogollum[q]['id'])
    print("Tipo:",eventogollum[q]['type'])
    print("Actor:")
    print("------- ID:",eventogollum[q]['actor']['id'])
    print("------- login:",eventogollum[q]['actor']['login'])
    print("------- avatar:",eventogollum[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventogollum[q]['repo']['id'])
    print("-----------name:",eventogollum[q]['repo']['name'])
    print("----------------public:",eventogollum[q]['public'])
print("================================================")
print("")

eventocomentariotema=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='IssueCommentEvent'):
        eventocomentariotema.append(miJSON[i])

for q in range (843):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventocomentariotema[q]['id'])
    print("Tipo:",eventocomentariotema[q]['type'])
    print("Actor:")
    print("------- ID:",eventocomentariotema[q]['actor']['id'])
    print("------- login:",eventocomentariotema[q]['actor']['login'])
    print("------- avatar:",eventocomentariotema[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventocomentariotema[q]['repo']['id'])
    print("-----------name:",eventocomentariotema[q]['repo']['name'])
    print("----------------public:",eventocomentariotema[q]['public'])
print("================================================")
print("")

eventoeliminado=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='DeleteEvent'):
        eventoeliminado.append(miJSON[i])

 
for q in range (259):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventoeliminado[q]['id'])
    print("Tipo:",eventoeliminado[q]['type'])
    print("Actor:")
    print("------- ID:",eventoeliminado[q]['actor']['id'])
    print("------- login:",eventoeliminado[q]['actor']['login'])
    print("------- avatar:",eventoeliminado[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventoeliminado[q]['repo']['id'])
    print("-----------name:",eventoeliminado[q]['repo']['name'])
    print("----------------public:",eventoeliminado[q]['public'])
print("================================================")
print("")

eventocomrevsoliextra=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='PullRequestReviewCommentEvent'):
        eventocomrevsoliextra.append(miJSON[i])
  

for q in range (135):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventocomrevsoliextra[q]['id'])
    print("Tipo:",eventocomrevsoliextra[q]['type'])
    print("Actor:")
    print("------- ID:",eventocomrevsoliextra[q]['actor']['id'])
    print("------- login:",eventocomrevsoliextra[q]['actor']['login'])
    print("------- avatar:",eventocomrevsoliextra[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventocomrevsoliextra[q]['repo']['id'])
    print("-----------name:",eventocomrevsoliextra[q]['repo']['name'])
    print("----------------public:",eventocomrevsoliextra[q]['public'])
print("================================================")
print("")

eventocomentarioconfir=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CommitCommentEvent'):
        eventocomentarioconfir.append(miJSON[i])
     


for q in range (72):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventocomentarioconfir[q]['id'])
    print("Tipo:",eventocomentarioconfir[q]['type'])
    print("Actor:")
    print("------- ID:",eventocomentarioconfir[q]['actor']['id'])
    print("------- login:",eventocomentarioconfir[q]['actor']['login'])
    print("------- avatar:",eventocomentarioconfir[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventocomentarioconfir[q]['repo']['id'])
    print("-----------name:",eventocomentarioconfir[q]['repo']['name'])
    print("----------------public:",eventocomentarioconfir[q]['public'])
print("================================================")
print("")


eventomiembro=[]#guarda datos del evento
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='MemberEvent'):
        eventomiembro.append(miJSON[i])
        

for q in range (24):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventomiembro[q]['id'])
    print("Tipo:",eventomiembro[q]['type'])
    print("Actor:")
    print("------- ID:",eventomiembro[q]['actor']['id'])
    print("------- login:",eventomiembro[q]['actor']['login'])
    print("------- avatar:",eventomiembro[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventomiembro[q]['repo']['id'])
    print("-----------name:",eventomiembro[q]['repo']['name'])
    print("----------------public:",eventomiembro[q]['public'])
print("================================================")
print("")

eventopublico=[]#guarda datos del evento

for i in range (len(miJSON)):
    if(miJSON[i]['type']=='PublicEvent'):
        eventopublico.append(miJSON[i])

      
for q in range (2):
    print("========================")
    print(":::: Evento # ",q+1 ,"::::")
    print("========================")
    print("ID: ",eventopublico[q]['id'])
    print("Tipo:",eventopublico[q]['type'])
    print("Actor:")
    print("------- ID:",eventopublico[q]['actor']['id'])
    print("------- login:",eventopublico[q]['actor']['login'])
    print("------- avatar:",eventopublico[q]['actor']['avatar_url'])
    print("Repo:")
    print("-----------ID:",eventopublico[q]['repo']['id'])
    print("-----------name:",eventopublico[q]['repo']['name'])
    print("----------------public:",eventopublico[q]['public'])
    print("================================================")
    print("")
#menu de opciones
print("===================MENU==========================")
print( "1.  Ver los tipos de eventos")
print( "2.  Crear")
print( "3.  Eliminar")
print( "4.  Actualizar")
print( "5.  revisar")
print( "6.  salir")
print( "================================================")

bool=True
while bool:
        opc=int(input("ingrese una opcion por favor : "))# le prmite eligir una opcion al usuario
        if opc==1:
                print("=================Nuestros Eventos==============")
                event=[]#guarda los nombres de los eventos 
                for i in range(len(miJSON)):#permite ir por cada uno
                 if miJSON[i]["type"] not in event:#si el nombre no se encuentra en la lista
                   event.append(miJSON[i]["type"])#con esto procedera aa garegarlo
        
                e=json.dumps(event,indent=1)#nos permite verlo mas ordenado
                print(e)#imprime
                print("================================================")
        elif opc==2:
            print("===============Crear o Añadir=================")
            raw=json.dumps(eventopublico,indent=1)
            print(raw)
            iddata=input("ingrese la id del evento: ")#añade algo a la lisat de evento publico
            new=input("que desea agregar a su evento")
            eventopublico.append(new)
            print(eventopublico)

        elif opc==3:
            print("===============ELIMINAR=================")
            print("================================================")


        elif opc==4:
                print("===============Actualizar=================")
                print("================================================")
        elif opc==5:
                print("===============Revisar=================")
                print(eventotenedor)
                print(eventopublico)
                print(eventoasunto)
                print(eventocomentarioconfir)#permite revisar los datos de cada evento
                print(eventocomentariotema)
                print(eventosolicitudextraccion)
                print(eventomiembro)
                print(eventoempuje)
                print(eventogollum)
                print(eventoeliminado)
                print(crearEventos)
                print(eventocomrevsoliextra)
                print(eventolanzamiento)
                print(verevento)
                print("v================================================")
           
    
            

        elif opc==6:
                 print(" ")
                 print("===============Salir=================")
                 print("")
                 print("Usted a decidido abandonar este programa")#se despide del usuario
                 print("           HASTA LA PROXIMA ;)          ")
                 print("          ······GOODBYE·······          ")
                 print("================================================")
                 break            

        
        #desarrollado por yurley botello T.I 1066085539
                
                