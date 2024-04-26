#!/usr/bin/python
# -*- coding: utf-8 -*-
import json#importar json

def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("infor.json","w") as outfile:
        json.dump(miData,outfile)

    
print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")
print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.Crear estudiante\n4.eliminar estudiante\n5.salir")
x=int(input("Cual opción escoges:"))
miInfo=[]
if(x==1):#revisar datos del estudiante
    miInfo=abrirArchivo()#abre el archivo
    contador = 0
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    for i in miInfo[1]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0
elif(x==2):#nos permite modificar cada dato a criterio del ususario
    miInfo=abrirArchivo()
    contador = 0
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    for i in miInfo[1]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0
    estudiante = int(input("Cual numero de identificacion vas a cambiar?"))#se le pregunta el numero de id al que desea actualizar
    print("Que te gustaría cambiar del estudiante:\n1.Nombre\n2.Apellido\n3.Edad\n4.Fecha de Nacimiento (DD-MM-AAAA)\n5.Cedula\n6.E-mail\n7.GitHub")
    datoCambiar=int(input("ingrese su opcion por favor: "))
    if (datoCambiar==1):#actualizacion del nombre
        nuevoNombre = input("Ingresa el nuevo nombre:")
        miInfo[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre#permite ghacer el recorrido por  hata posicionarse en la indicada
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador=0
    if(datoCambiar==2):#actualizacion del apellido
        nuevoApellido = input("Ingresa el nuevo apellido:")
        miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
        guardarArchivo(miInfo)#nos guarda lo anterior en la info
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()#nos permite abrir lo anteriormente guardado
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador=0
    if(datoCambiar==3):#actualizacion de la edad
        nuevaEdad = input("Ingresa el nuevo edad:")
        miInfo[0]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador=0

    if(datoCambiar==4):#actualizacion de la fecha de nacimiento
        nuevaFechadeNacimiento = input("Ingresa la nueva Fecha de Nacimiento")
        miInfo[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFechadeNacimiento
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador=0
    if(datoCambiar==5):#actualizacion de la cedula
        nuevaCedula= input("Ingrese el nuevo numero de cedula")
        miInfo[0]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador=0
    
    if(datoCambiar==6):#actualizacion del email
        nuevoEmail= input("Ingrese el nuevo e-mail")
        miInfo[0]["estudiantes"][estudiante-1]["email"] = nuevoEmail#actualiza el dato haciendo un recorrido hasta llegaral indicado por el usuario
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()#abre el archivo
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("") 
    contador=0  
    if(datoCambiar==7):#actualizacion del github
        nuevoGithub= input("Ingrese el nuevo github")
        miInfo[0]["estudiantes"][estudiante-1]["github"] = nuevoGithub
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador=0
elif (x==3):
    print("=====Crear Estudiantes========")
    
    #guarda en  ne_students los datos que necesita para crear uno nuevo sobre algun estudante
   
    new_estudent=[
        { #le pide al usuario que ingrese sus datos
            "id":str(input("agregue la id del nuevo estudiante:")),
            "nombre":input("agrege el nombre del nuevo estudiante: "),
            "apellido":input("agregue el apellido del nuevo estudiante: "),
            "edad":input("agregue la edad del nuevo estudiante: "),
            "fechaNacimiento":input("agregue la fecha de nacimiento del nuevo estudiante: "),
            "cedula":input("agregue la cedula del nuevo estudiante:"),
            "email":input("agregue el email del nuevo estudiante: "),
            "github":input("agregue el github del nuevo estudiante"),
        }
    ]
    print("su nuevo estudiante a sido creado")
    guardarArchivo(miData=new_estudent)#esos datos los guardara  en mi data
    contador=0
    miInfo=abrirArchivo()
   
    for i in new_estudent:#nos muestra lo anterior creado
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0


         #with open ("info.json","w")as archi:
            # json.dump(new_estudent,archi)
elif (x==4):
    print("======Eliminar Estudiante======")
    id=int(input("ingrese la id que desea eliminar: "))

    del miInfo[id]
    guardarArchivo(miInfo)
    
    with open ("delete.json","w")as archi:
       json.dump(miInfo,archi)
elif( x==5):
    print("usted ha abandonado este programa")#se despide del usuario
    print("adioos!! ;)")
  
#desarrollado por yurley botello -camper T.I 1066085539

    
    
   
