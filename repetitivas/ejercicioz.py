


    #haga un algoritmoo que establezca un ciclo  "
for i in range(1, 8):
    if i == 8 :
          print("completado.")
          break
    print("valor:", i)
print("completado.")



for i in range(1, 20):
     if i %3==0:
          continue
     print(i)
''''''''
# ejercicio 1 de la guia
positivo= 0
negativo= 0
neutros= 0
for i in range(20):
    numero= int(input ("ingrese un numero:")) 

    if numero>=0: 
         positivo += 1
    elif numero < 0 :
         negativo += 1
    else:
         neutros += 1
print("cantidad de numeros:", positivo)
print("cantidad de numeros",negativo)
print("cantidad de numeros ", neutros)
    


''''''''
#lee 10 numeros negativos y convertirlos a positivos e imprimir la suma de dichos numeros.

suma_positivos= 0
for i in range(10):
     numero=int(input("ingrese un numero negativo:"))
     if numero < 0:
          numero *= -1
          suma_positivos += numero
          print("la suma de los numeros positivos es:",suma_positivos)


''''''''


# suponga que se tiene un conjunto de calificaciones de un grupo  de 20 alumnos. realizar un algoritmo para calcular el promedio y la calificacion mas alta y mas baja de todo el grupo
sumacalificaciones= 0
cantidadcalificaciones=0
calificacionmenor=5
calificacionMayor=0

for i in range(1,4):
     calificaciones=float(input("ingrese la calificacion final"))
     if calificaciones<calificacionmenor:
          calificacionmenor=calificaciones
     elif calificaciones>calificacionMayor:
          calificacionMayor=calificaciones
          cantidadcalificaciones +=1
          sumacalificaciones+=calificaciones
          promedio=sumacalificaciones/cantidadcalificaciones

          print("el promedio del grado es :", promedio)
          print("calificacion mas alta:", calificacionMayor)
          print("calificacion mas baja es :", calificacionmenor)
''''''''

#calcular e imprimir la tabla de multriplicar de un numero cualquiera, el cual se digitara por teclado. imprimir el multiplicando, el multiplicador y el producto.


numero= int(input("ingrese el numero de la tabla de multiplicar"))

for i in range(1,11):
     print(f"{numero} x {i} = {numero * i}")









---------------


#una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños , jovenes , adultos y ancianos que existen en su zona las categorias se determinar de acuerdo a la tabla











          
        
