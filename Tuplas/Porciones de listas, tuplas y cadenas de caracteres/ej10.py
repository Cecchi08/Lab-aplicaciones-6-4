def cargar_lista():
    lista = []
    for i in range(10):
        num = int(input(f"Ingrese el número {i+1}: "))
        lista.append(num)
    return lista

def primera_mitad(lista):
    mitad = len(lista) // 2
    return lista[:mitad]

def imprimir_lista(lista):
    print("Elementos de la lista:")
    for elemento in lista:
        print(elemento)

lista_completa = cargar_lista()
mitad_lista = primera_mitad(lista_completa)
print("\nLista completa:")
imprimir_lista(lista_completa)
print("\nPrimera mitad de la lista:")
imprimir_lista(mitad_lista)
