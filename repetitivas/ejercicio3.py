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
          