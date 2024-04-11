import random
randonnum = random.randint(1,100) #elige el numero al azar

inten=0 # cantidad de intentos

print("intenta adivinar el numero utilzando pocos intentos")

while  inten < 6:
   print(f" intento {inten}")

   inte=int(input()) #ingresa tu numero
   inten += 1

   if inte < randonnum:
      print("tu intento es muy bajo al numero") # verifica si el numero es alto al adivinar

   elif inte > randonnum:
      print(" tu numero es muy alto al numero") # verifica si el numero a adivinar es  bajo

   else:
      break#rompe el bucle

if inte==randonnum:
   print(f"adivinastes el numero y es {randonnum}")#te dice si tu has adivinado el numero
else:
   print(f"tu has perdido el numero es:{randonnum}")



 #Desarrolado por yurley Botello
