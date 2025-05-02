paises = []
for i in range(5):
    nombre = input(f"Ingrese el nombre del país {i+1}: ")
    paises.append(nombre)

paises.sort()

print("\nLista de países ordenada alfabéticamente:")
for pais in paises:
    print(pais)
