import random
secretnu = random.randint(1,100) #elige el numero al azar

ins=0 # cantidad de intentos

print("intenta adivinar el numero")

while  ins < 10:
   print(f" intento {ins}")

   veces=int(input()) #ingresa tu numero
   ins += 1

   if veces < secretnu:
      print("tu intento es muy bajo al numero") # verifica si el numero es alto al adivinar

   elif veces> secretnu:
      print(" tu numero es muy alto al numero") # verifica si el numero a adivinar es  bajo

   else:
      break #rompe el bucle

if veces==secretnu:
   print(f"adivinastes el numero ¡¡Felicidadessss!!")#te dice si tu has adivinado el numero
else:
   print(f"tu has perdido el numero era:{secretnu}")  #te dice si perdistes

   print("tu numero de intentos fueron: ")

ins=ins
print(f"tu numero de intentos fueron: {ins} ")


 #Desarrolado por yurley Botello