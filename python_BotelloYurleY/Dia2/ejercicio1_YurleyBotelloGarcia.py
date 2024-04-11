print("--------------------------")
print("______BIENVENIDO__________")
print("---------------------------")
print(" la secuencia de fibonacci se encarga de sumar los numeros con el anterior para asi obtener el siguiente.")


num=int(input("ingrese un valor: "))  # pedimos al usuario ingreasar valores

def fi(num): # Definimos funcion
        
 if num < 2:
   return num
 
 else:
   return fi(num-1) + fi(num-2)
 
 
fi(num)   # llamamos la funcion



for x in range(num):  # indica hasta donde se realizara 
 print(fi(x))



print("hemos terminado") #indica que se a cumplido la secuencia de fibonacci
print("desea continuar si/no") # le pregunta si desea continuar
i=str(input())
b=True
while b:
  if i=="no":
    print("adios!!")
    break 

  elif i =="si":
    print("continuemos")
    break
  
num=int(input("ingrese un valor: "))

def fi(num):
        
 if num < 2:
   return num
 
 else:
   return fi(num-1) + fi(num-2)
 


fi(num)

for x in range(num):
 print(fi(x))
 

 


  #Desarrolado por yurley Botello



        
        



    




 



 
   


    
 

   

 


