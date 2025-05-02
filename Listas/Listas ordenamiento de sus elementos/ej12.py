numeros = []
for i in range(5):
    valor = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(valor)

numeros.sort()
print("\nLista ordenada de menor a mayor:")
print(numeros)

numeros.sort(reverse=True)
print("\nLista ordenada de mayor a menor:")
print(numeros)
