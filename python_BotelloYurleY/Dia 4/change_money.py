 
print("...........................................................")
print("_________________-WELCOME MONEY CHANGE_____________________")
print("...........................................................")


coins=int(input("\ningrese su dinero porfavor : "))#permite ingresar  el numero del dinero a cambiar a monedas

moneda=1#valor de la moneda 1
monedas=5#valor de la moneda 2
monedita=10#valor de la moneda 3
cont1=0#contador 
cont2=0#contador
cont3=0#contador
print("::::::::::::::::::::::::::::::::::::::::::::") 
monedit=(coins//monedita)#se divide la cantidad de monedas por monedas de 10 para sacr cuantas hay en es cantidad

for a in range (monedit):#luego la cantidad que hay se ponen como rango
    cont1+=1#se agrega el primer contador
    co=monedita#se le da una variable a monedita 10
    print(co)#se imprime

    m=monedit*10#se hace la multiplicacion para sacr el total de las monedas anteriores
    moni=(coins-m)//monedas#se resta el total anterior con la cantidad inicial y se divide por monedas que en este caso es 5

for b in range(moni):#el valor de la division anterior se pone como rangp
        cont2+=1#utilizamos un segundo contador
        coin=monedas#otra variable para la monedas de 5 
        print(coin)#imprimimos el dato


        

        ni=moni*5#multiplicamos el resultao anterior por 5 para sacar la catidad
        mo=m+ni#sumas el valor de la primera multiplicacion y la segunda para sumar y acumular en una variable
        monis=(coins-mo)//moneda# le restaremos la suma anterior a la cantidad inicial y dividiremos en monedas  en este caso 1
for c in range(monis):#agregamos el valor de la divisio al rango
            cont3=cont3+1#utilizamos un tercer contador
            ney=moneda#una anueva variable a la moneda equivalente a 1
           
            print(ney) #imprimimos el dato
print("")
print("::::::::::::::::::::::::::::::::::::::::::::")           
print(f"{monedit} monedas de 10")#cantidad de monedas de 10 a imprimir
print(f"{moni} monedas de 5")#cantidad de monedas de 5 a imprimir
print(f"{monis} monedas de 1")#cantidad de monedas de 1 a imprimir
print("::::::::::::::::::::::::::::::::::::::::::::") 

 #desarrollado por Garcia Botello Yurley  T.T 1066085539sssss


  