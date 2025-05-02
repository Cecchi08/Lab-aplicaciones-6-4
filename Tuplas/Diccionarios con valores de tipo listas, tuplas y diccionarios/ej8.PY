alumnos = {}

def cargar_alumnos():
    for i in range(3):
        dni = input(f"Ingrese el DNI del alumno {i+1}: ")
        materias = []
        cantidad_materias = int(input(f"¿Cuántas materias cursa el alumno con DNI {dni}? "))
        
        for _ in range(cantidad_materias):
            materia = input("Ingrese el nombre de la materia: ")
            nota = float(input(f"Ingrese la nota obtenida en {materia}: "))
            materias.append((materia, nota))
        
        alumnos[dni] = materias

def listar_alumnos():
    print("\nListado de todos los alumnos y sus notas:")
    for dni, materias in alumnos.items():
        print(f"DNI: {dni}")
        for materia, nota in materias:
            print(f"  - Materia: {materia}, Nota: {nota:.2f}")

def consultar_alumno():
    dni = input("\nIngrese el DNI del alumno para consultar: ")
    if dni in alumnos:
        print(f"Materias y notas del alumno con DNI {dni}:")
        for materia, nota in alumnos[dni]:
            print(f"  - Materia: {materia}, Nota: {nota:.2f}")
    else:
        print(f"No se encontró un alumno con el DNI {dni}")

cargar_alumnos()
listar_alumnos()
consultar_alumno()
