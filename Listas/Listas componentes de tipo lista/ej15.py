lista = [[4, 12, 5, 66], [14, 6, 25], [3, 4, 5, 67, 89, 23, 1], [78, 56]]

print("Lista original:")
print(lista)

for sublista in lista:  
    for i in range(len(sublista)):
        if sublista[i] > 10:
            sublista[i] = 0

print("\nLista después de modificar los elementos mayores a 10:")
print(lista)
