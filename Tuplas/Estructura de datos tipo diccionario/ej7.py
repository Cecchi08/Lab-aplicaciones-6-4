personas = {}

def cargar_personas():
    for i in range(4):
        doc = input(f"Ingrese el número de documento de la persona {i+1}: ")
        nombre = input(f"Ingrese el nombre de la persona con documento {doc}: ")
        personas[doc] = nombre

def listar_personas():
    print("\nListado completo de personas:")
    for doc, nombre in personas.items():
        print(f"Documento: {doc}, Nombre: {nombre}")

def consultar_persona():
    doc = input("\nIngrese el número de documento para consultar el nombre: ")
    if doc in personas:
        print(f"El nombre de la persona con documento {doc} es: {personas[doc]}")
    else:
        print(f"No se encontró ninguna persona con el documento {doc}")

cargar_personas()
listar_personas()
consultar_persona()
