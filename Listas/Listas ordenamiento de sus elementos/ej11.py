cantidad = int(input("Ingrese la cantidad de empleados: "))

sueldos = []
for i in range(cantidad):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i + 1}: "))
    sueldos.append(sueldo)

sueldos.sort()

print("\nLista de sueldos ordenada de menor a mayor:")
for sueldo in sueldos:
    print(sueldo)
