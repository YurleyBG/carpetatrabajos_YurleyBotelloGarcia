producto=("manzanas rojas", "manzanas verdes","manazanas amarillas")# productos disponibles
          
precio=2500#precio de cada manzna
cantavail=100#cantidad disponible
carrito=[]#lista vacia "carrito"
#bienvenida ala usuario
print(" ==============Bienvenido=================")
print("solo ventas de manzanas,rojas, verdes y amarillas")
print("escoje a tu preferencia")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::")
bool=True
while bool:#ciclo while para que se repita mientras se cumpla la condicion
    #imprimir productos mientras , precio y cantidad, la cantidad debera ir disminuyendo por cada compra
    print("\nproductos: " ,producto,"precio : " ,precio,"cantidad disponible: " ,cantavail,) 
    
    for i in  range(1):#utilizamos un ciclo for 
     
     
     cant=int(input("cuantas manzanas desea comprar:  "))#le pidimos al usuario ingresar la cantidad
     
     if cant<cantavail:#utilizamos un if para verificar si  la cantidad pedida por el usuario se encuentra o no
      nom=input("ingrese el nombre de la manzana de su preferencia:" )#si se encuentra  pidira al ususraio la cantidad
      cantavail=cantavail-cant# esto permite irle restando a la cantidad la cantidad pedida del usuario
      d=cant*precio#permite sacar el precio total que debera pagar el usuario


      carrito=[nom,cant,d]#aqui nos permite guardarlo anterior en nuestra lista anteriormente vacia
      print(carrito)#imprimimos la lista para verificaque si se haya guardaado
      
     else:# si la condicion anterior de la cantidad no se cumple se imprimira el siguiente mensaje
       print ("cantidad no disponible")
    
    
bool=False
#desarrollado por yurley botekllo garcia T.I 1066085539