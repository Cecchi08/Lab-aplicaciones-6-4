def cargar_candidatos():
    candidatos = []
    for i in range(3):
        nombre = input(f"Ingrese el nombre del candidato {i+1}: ")
        votos_provincias = []
        cantidad_provincias = int(input(f"Ingrese cuántas provincias desea cargar para {nombre}: "))
        for j in range(cantidad_provincias):
            provincia = input(f"Nombre de la provincia {j+1}: ")
            votos = int(input(f"Cantidad de votos en {provincia}: "))
            votos_provincias.append((provincia, votos))
        candidatos.append([nombre, votos_provincias])
    return candidatos

def imprimir_totales(candidatos):
    print("\nCantidad total de votos por candidato:")
    for candidato in candidatos:
        nombre = candidato[0]
        votos = candidato[1]
        total = sum(cant for _, cant in votos)
        print(f"{nombre}: {total} votos")

candidatos = cargar_candidatos()
imprimir_totales(candidatos)
