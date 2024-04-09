#--------------------------------
#---- DIA 1 CHEAT SHEET PYTHON ------
#--------------------------------

#Imprimir hola mundo
print("Hola mundoooooooooooooo!!!")

#Datos primitivos

#Numero
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la infomarcion
print("¿ingrese su edad?")
edad= input()
print(edad)

#Conversion de tipos de variable
v=2
print(type(v))#tipo de variable a cambiar
print(float(v))#tipo al que se convierte

g=46.5
print(type(g))#tipo de variable a cambiar
print(int(g))#tipo al que se convierte

t="hola"
print(type(t))#tipo de variable a cambiar
print(bool(t))#tipo al que se convierte

b=False
print(type(b))#tipo de variable a cambiar
print(str(b))#tipo al que se convierte



#Bucles For y While

#Bucles For 
nombre=("maria", "luis","kiara", "carlo")
for i in nombre:
    print(i)
    if i == "carlos":
        break
    print(i)


#Bucles While
i=0
while i < 4:
    print(i)
    if i==3:
        break
    i+= 1


#Funciones (4 Tipos)

#Desarrollado por Yurley Botello Garcia - T.I 1066085539