# Inicializar contadores para cada rango de calificaciones
menor_a_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_a_80 = 0

# Solicitar calificaciones de los 10 estudiantes
for i in range(1, 11):
    calificacion = int(input(f"Ingrese la calificación del estudiante {i}: "))
    
    
    if calificacion < 50:
        menor_a_50 += 1
    elif calificacion >= 50 and calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion >= 70 and calificacion < 80:
        entre_70_y_80 += 1
    else:
        mayor_a_80 += 1


print("Estudiantes con calificaciones menores a 50:", menor_a_50)
print("Estudiantes con calificaciones entre 50 y 70:", entre_50_y_70)
print("Estudiantes con calificaciones entre 70 y 80:", entre_70_y_80)
print("Estudiantes con calificaciones mayores a 80:", mayor_a_80)
