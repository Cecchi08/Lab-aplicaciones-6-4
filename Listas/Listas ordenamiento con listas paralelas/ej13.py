paises = []
habitantes = []

for i in range(5):
    nombre = input(f"Ingrese el nombre del país {i+1}: ")
    poblacion = int(input(f"Ingrese la cantidad de habitantes de {nombre}: "))
    paises.append(nombre)
    habitantes.append(poblacion)

pais_hab = list(zip(paises, habitantes))
pais_hab.sort(key=lambda x: x[0])

print("\nListado ordenado alfabéticamente por país:")
for pais, hab in pais_hab:
    print(f"{pais}: {hab} habitantes")

pais_hab.sort(key=lambda x: x[1], reverse=True)

print("\nListado ordenado por cantidad de habitantes (de mayor a menor):")
for pais, hab in pais_hab:
    print(f"{pais}: {hab} habitantes")
