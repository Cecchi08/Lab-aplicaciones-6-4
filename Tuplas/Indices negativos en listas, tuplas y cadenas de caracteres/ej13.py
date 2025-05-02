def cargar_palabras():
    lista = []
    for i in range(5):
        palabra = input(f"Ingrese la palabra {i + 1}: ")
        lista.append(palabra)
    return lista

def intercambiar_primera_ultima(lista):
    lista[0], lista[-1] = lista[-1], lista[0]

def imprimir_lista(lista):
    print("Contenido de la lista:")
    for palabra in lista:
        print(palabra)

palabras = cargar_palabras()
intercambiar_primera_ultima(palabras)
imprimir_lista(palabras)
