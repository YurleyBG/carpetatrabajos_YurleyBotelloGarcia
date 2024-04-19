print("-----------------------------------------------------------")
print("..............BIENVENIDO A NUESTRA TIENDA..................")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

carrito={}

menu_productos={
    "producto 1":{
    "pro1":"arroz",
    "precio":4500,
    "ID":11237
    },
    "producto 2":{
    "pro2":"azucar",
    "precio":3500,
    "ID":77891
    },
    "producto 3":{
    "pro3":"cafe",
    "precio":8000,
    "ID":66739
    },
    "producto 4":{
    "pro4":"panela",
    "precio":10000,
    "ID":99845
    },
    "producto 5":{
    "pro5":"carne",
    "precio":14000,
    "ID":34562
    },

    "producto 6":{
    "pro6":"pollo",
    "precio":7500,
    "ID":34575
    },
    "producto 7":{
    "pro7":"manzana",
    "precio":2500,
    "ID":12389
    },
    "producto 8":{
    "pro8":"fresa",
    "precio":5000,
    "ID":36789
    },
    "producto 9":{
    "pro9":"platano",
    "precio":3000,
    "ID":99002
    },
    "producto 10":{
    "pro10":"huevos",
    "precio":14000,
    "ID":98122
    }
}


print("::::::::::::::::::::MENU DE OPCIONES:::::::::::::::::::::::")
print("1. Agregar productos productos al carrito")
print("2. ver contenido del carrito")
print("3. obtener el total de la compra")
print("4. finalizar compra y salir")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

bob=True
while bob :

    opc= int(input())

    if opc==1:
        print("======AGREGAR PRODUCTOS AL CARRITO============")
        print(" ")

        print("========MENU=======")
        for producticos in menu_productos.items():
            print(producticos)
        
             
       
       
        prodagre=input("\nque productos desea agregar al carrito de comprar INGRESE SU IDENTIFICADOR : ")
        cantpro=int(input("ingrese su cantidad : "))



        if prodagre==menu_productos:
           # carrito= menu_productos.pop(prodagre, 0)
            

            carrito[prodagre]=menu_productos[prodagre]
            carrito[prodagre]=cantpro
            cont=cont+[prodagre]*cantpro
            print[carrito]

        
    elif opc==2:
        print("==========mirar productos del carrito===================")

        

        print=(carrito)
        
        


    elif opc==3:
        print("=========TOTAL DE SU COMPRA==========")



    
    elif opc==4:
        print("=================================")
        print("Haz finalizado tu compra")
        print("adiosss!!!")
        print("----------------------------------")
        break
bob=False
 
#desarrollado por   yurley botello TI 1066085539 y nilson  carvajal  TI 1093907710 :)