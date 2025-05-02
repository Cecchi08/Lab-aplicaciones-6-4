
productos = []

def cargar_productos():
    for i in range(5):
        nombre = input(f"Ingrese el nombre del producto {i+1}: ")
        precio = float(input(f"Ingrese el precio de {nombre}: "))
        productos.append((nombre, precio))

def listar_productos():
    print("\nListado de productos y precios:")
    for producto in productos:
        nombre, precio = producto
        print(f"{nombre}: ${precio:.2f}")

def productos_rango_precio(min_precio, max_precio):
    print(f"\nProductos con precios entre ${min_precio} y ${max_precio}:")
    for producto in productos:
        nombre, precio = producto
        if min_precio <= precio <= max_precio:
            print(f"{nombre}: ${precio:.2f}")

# Bloque principal
cargar_productos()
listar_productos()
productos_rango_precio(10, 15)
