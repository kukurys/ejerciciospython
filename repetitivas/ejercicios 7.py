#.un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
#algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e
#imprima:

import random

qualification1 = 0
qualification2 = 0
qualification3 = 0
qualification4 = 0

for estudiante in range(23):

    estudiante = random.randint(1, 100);

    if estudiante <= 50 :
        qualification4 += 1
    elif estudiante >= 50 and estudiante <= 70: 
         qualification3 += 1
    elif estudiante >= 70 and estudiante <= 80 :
        qualification2 += 1
    elif estudiante >= 80 :
        qualification1 += 1

print(f'{qualification1} Obtuvieron una calificacion mayor a 80');
print(f'{qualification2} Obtuvieron una calificacion mayor a 70 y menor 80');
print(f'{qualification3} Obtuvieron una calificacion mayor a 50 y menor a 70');
print(f'{qualification4} Obtuvieron una calificacion menor a 50');


""""""


#Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos. 
import random

edadHombre = 0
numHombre = 0 

edadMujer=0
numMujer=0

for i in range(40):
    sexo = random.choice(['hombre' , 'mujer'])
     
    if sexo == 'hombre':
         edad = random.randint(15, 50)
         numHombre +=1
         edadHombre += edad
    else:
        edad=random.randint(15, 50)
        numMujer +=1
        edadMujer += edad
        
edadPromedioHombre = int(edadHombre / numHombre)
edadPromedioMujer = int(edadMujer / numMujer)

print(f'la edad promedio de los hombres es: {edadPromedioHombre}')
print(f'la edad promedio de las mujeres es: {edadPromedioMujer}')





""""""""""""

