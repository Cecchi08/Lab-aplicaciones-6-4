nombres = []
for i in range(5):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    nombres.append(nombre)

menor = min(nombres)

print("\nEl nombre menor en orden alfabético es:", menor)
