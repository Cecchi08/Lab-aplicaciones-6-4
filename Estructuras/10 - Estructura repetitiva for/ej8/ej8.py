turno_mañana = 0
turno_tarde = 0
turno_noche = 0
suma = 0

for i in range(5):
    edad = int(input("Ingrese la edad "))
    suma += edad
    
promedio_mañana = suma / 5

suma = 0
for i in range(6):
    edad = int(input("Ingrese la edad "))
    suma += edad
    
promedio_tarde = suma / 6

suma = 0

for i in range(11):
    edad = int(input("Ingrese la edad "))
    suma += edad
    
promedio_noche = suma / 11

print("El promedio de la mañana es ", promedio_mañana)
print("El promedio de la tarde es ", promedio_tarde)
print("El promedio de la noche es ", promedio_noche)

if promedio_noche < promedio_mañana > promedio_tarde:
    print("El mayor promedio es del turno mañana")

elif promedio_noche < promedio_tarde > promedio_mañana:
    print("El promedio mas grande es el de la tarde")
else:
    print("El promedio mas grande es el de la noche")
    

