productos = []
precios = []

for i in range(5):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    productos.append(nombre)
    precios.append(precio)

precio_referencia = precios[0]
contador = 0

for i in range(1, 5):
    if precios[i] > precio_referencia:
        contador += 1

print(f"\nCantidad de productos con precio mayor al primero ({productos[0]}): {contador}")
