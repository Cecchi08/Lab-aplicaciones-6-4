nombres = []
notas = []

for i in range(4):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    nombres.append(nombre)
    notas.append(nota)

print("\nListado de alumnos:")
muy_buenos = 0

for i in range(4):
    condicion = ""
    if notas[i] >= 8:
        condicion = "Muy Bueno"
        muy_buenos += 1
    elif notas[i] >= 4:
        condicion = "Bueno"
    else:
        condicion = "Insuficiente"
    
    print(f"{nombres[i]} - Nota: {notas[i]} - Condición: {condicion}")

print(f"\nCantidad de alumnos con condición 'Muy Bueno': {muy_buenos}")
