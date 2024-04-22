nums=[]#lista vacia 
list=input().split();nums=list#permite al usuario agregar los datos a la lista, lo segundo ingresa lo que el usuario escribio a la lista vacia
print(nums)#imprime la lista
target=input()#permite ingresar el objetivo

for i in range(len(nums)):#utilizamos un cilo for para que vaya por cada uno de los numeros de a lista
    num=nums[i]#nos indica el indice de los numeros de la lista
if target==num:#utilizamos u si para mirar si el numero objetivo del usuario se encuentra
        print(nums.index(target))#nos imprime la posicion del numero objetivo del usuario
elif target not in num:#utilizamos otro si para que si el numero del usuario no se encuentra
        nums.append(target)#lo guarde en la lista 
        n=sorted(nums)#utilizamos el sorted para ordenar todo los numeros nuevos ingresados de manera ascendente 
        print(n.index(target))#imprimimos nuevamente el indice del numero indicado
#Desarrollado por Yurley Botello Garcia T.I 1066085539
        

