def cargar_empleados():
    empleados = []
    for i in range(5):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        sueldos = []
        for j in range(3):
            sueldo = float(input(f"Ingrese el sueldo del mes {j+1} para {nombre}: "))
            sueldos.append(sueldo)
        empleados.append([nombre, tuple(sueldos)])
    return empleados

def total_por_empleado(empleados):
    print("\nMonto total cobrado por cada empleado:")
    for empleado in empleados:
        nombre = empleado[0]
        sueldos = empleado[1]
        total = sum(sueldos)
        print(f"{nombre}: ${total:.2f}")

def ingresos_mayores_a_10000(empleados):
    print("\nEmpleados con ingreso trimestral mayor a $10000:")
    for empleado in empleados:
        nombre = empleado[0]
        sueldos = empleado[1]
        if sum(sueldos) > 10000:
            print(nombre)

empleados = cargar_empleados()
total_por_empleado(empleados)
ingresos_mayores_a_10000(empleados)
