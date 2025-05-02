def gestionar_empleados():
    cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))

    nombres = []
    sueldos = []

    for i in range(cantidad_empleados):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        sueldo = float(input(f"Ingrese el sueldo de {nombre}: "))
        nombres.append(nombre)
        sueldos.append(sueldo)

    print("\nEmpleados y sus sueldos antes de eliminar:")
    for i in range(cantidad_empleados):
        print(f"{nombres[i]}: {sueldos[i]}")

    indices_a_eliminar = [i for i in range(len(sueldos)) if sueldos[i] > 10000]

    for i in reversed(indices_a_eliminar):
        del nombres[i]
        del sueldos[i]

    print("\nEmpleados y sus sueldos después de eliminar:")
    for i in range(len(nombres)):
        print(f"{nombres[i]}: {sueldos[i]}")

gestionar_empleados()
