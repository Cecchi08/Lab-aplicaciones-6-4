empleados = ["Juan", "María", "Carlos"]
inasistencias = [
    [2, 4, 6], 
    [1, 3, 5], 
    [3, 7, 8] 
]

print("Nombres de empleados y los días que faltaron:")
for i in range(len(empleados)):
    print(f"{empleados[i]} faltó los días: {inasistencias[i]}")

inasistencias_count = [len(dias) for dias in inasistencias]

print("\nCantidad de inasistencias por empleado:")
for i in range(len(empleados)):
    print(f"{empleados[i]} tuvo {inasistencias_count[i]} inasistencias")

min_inasistencias = min(inasistencias_count)
empleados_menos_faltas = [empleados[i] for i in range(len(empleados)) if inasistencias_count[i] == min_inasistencias]

print("\nEmpleado(s) que faltaron menos días:")
for empleado in empleados_menos_faltas:
    print(empleado)
