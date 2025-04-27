productos = {
    "nombre" : [],
    "precio" : [], 
    "stock" : []
}
    
def agregar_productos():
    producto_nombre = (input("Ingrese el nombre del producto a agregar "))
    producto_precio = int(input("Ingrese el precio del producto "))
    producto_stock = int(input("Ingrese el stock del producto"))
    productos["nombre"].append(producto_nombre)
    productos["precio"].append(producto_precio)
    productos["stock"].append(producto_stock)

def listar_productos():
    for i in range(len(productos["nombre"])):
        print(f"Producto {i+1}:")
        print(f"  Nombre: {productos['nombre'][i]}")
        print(f"  Precio: {productos['precio'][i]}")
        print(f"  Stock: {productos['stock'][i]}")
        print()    
        
def buscar_productos():
    producto = input("Ingrese el nombre del producto a buscar ")
    for i in range(len(productos["nombre"][i])):
        if productos["nombre"][i] == producto:
             print(f"Producto encontrado:")
             print(f"  Nombre: {productos['nombre'][i]}")
        else:
            print("No hay ningun producto con el nombre ", productos["nombre"][i])
        
def actualizar_productos():
    producto = input("Ingrese el nombre del producto a actualizar ")
    nuevo_stock = int(input("Ingrese el nuevo stock del producto "))
    for i in range(len(productos["nombre"][i])):
        if productos["nombre"][i] == producto:
            productos["stock"][i] = nuevo_stock
            print("Producto actualizado")