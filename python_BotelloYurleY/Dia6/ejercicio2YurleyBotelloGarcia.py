
nums= [-8,-6,7,10]#indica los valores enteros de la lista 
target=1#indica el valor objetivo,

print(f"target",(target)) #nos imprime nuestro valor objetivo en la consola


for i in range(0,len(nums),1):#utilizamos un bucle for para limitar y seguir un ciclo

    
    if -100 <= nums[i] <= 100:#permite que nums valga tanto como positivo como negativo
         print(nums)#imprime los nums en la terminal
    elif -100 <= target <= 100: #permite que target valga positivo como negativp
        print(target)#imprime target
    break#rompe este ciclo y pasa al siguiente
        
for i  in range(len(nums)):#otro ciclo for para limitar y poder realizar la suma
    if nums[i]+nums[i+1]==target:#realiza la suma

        print(f"posiciones : {i}, {i+1}")#indica la posicion en donde se encuentra los numero que al sumarse dan el mismo resultado del objetivo

        break#termina el ciclo


      #Desarrollado por Garcia Botello Yurley  T.T 1066085539 :)
    

       
   
      