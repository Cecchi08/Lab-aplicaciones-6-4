empleados = {}

def cargar_empleados():
    cantidad = int(input("Ingrese la cantidad de empleados a cargar: "))
    for _ in range(cantidad):
        legajo = input("Ingrese número de legajo: ")
        nombre = input("Ingrese nombre del empleado: ")
        profesion = input("Ingrese profesión del empleado: ")
        sueldo = float(input("Ingrese sueldo del empleado: "))
        empleados[legajo] = [nombre, profesion, sueldo]
    print("\nCarga finalizada.\n")

def modificar_sueldo():
    legajo = input("Ingrese el número de legajo del empleado: ")
    if legajo in empleados:
        nuevo_sueldo = float(input(f"Ingrese el nuevo sueldo para {empleados[legajo][0]}: "))
        empleados[legajo][2] = nuevo_sueldo
        print("Sueldo actualizado correctamente.\n")
    else:
        print("No se encontró un empleado con ese legajo.\n")

def mostrar_analistas():
    print("Empleados con profesión 'analista de sistemas':")
    encontrados = False
    for legajo, datos in empleados.items():
        nombre, profesion, sueldo = datos
        if profesion.lower() == "analista de sistemas":
            print(f"Legajo: {legajo}, Nombre: {nombre}, Profesión: {profesion}, Sueldo: {sueldo}")
            encontrados = True
    if not encontrados:
        print("No se encontraron empleados con esa profesión.\n")

cargar_empleados()
modificar_sueldo()
mostrar_analistas()
