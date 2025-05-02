numeros = []
for i in range(5):
    valor = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(valor)

mayor = max(numeros)

cantidad = numeros.count(mayor)

print("\nEl mayor valor es:", mayor)

if cantidad > 1:
    print("El mayor valor se repite en la lista.")
else:
    print("El mayor valor no se repite.")
