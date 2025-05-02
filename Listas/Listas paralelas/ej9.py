lista1 = []
lista2 = []

print("Cargando la primera lista:")
for i in range(4):
    num = int(input(f"Ingrese el elemento {i+1} de la primera lista: "))
    lista1.append(num)

print("\nCargando la segunda lista:")
for i in range(4):
    num = int(input(f"Ingrese el elemento {i+1} de la segunda lista: "))
    lista2.append(num)

lista_suma = []
for i in range(4):
    suma = lista1[i] + lista2[i]
    lista_suma.append(suma)

print("\nLista con la suma de elementos en la misma posición:")
print(lista_suma)
