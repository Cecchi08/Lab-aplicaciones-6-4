import productos
cant_operaciones = int(input("Bienvenido, cuantas operaciones quiere realizar "))
for i in range(cant_operaciones):
    operacion = input("Bienvenido al sistema de inventario, que operacion quieres realizar: [A] agregar productos, [L] listar productos, [B] buscar productos por nombre [S] actualizar stock, [E] salir ")
    match operacion:
        case 'A':
            productos.agregar_productos()
        case 'L':
            productos.listar_productos()
        case 'B':
            productos.buscar_productos()
        case 'S':
            productos.actualizar_productos()
        case 'E': 
            print("Gracias por elegir nuestros servicios")
            break