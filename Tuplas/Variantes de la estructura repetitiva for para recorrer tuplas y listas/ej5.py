palabras = []
mayoresA5 = []

def cargarDatos(): 
    cantidad = int(input("Ingrese la cantidad de palabras: "))
    for i in range(cantidad):
        palabra = input("Ingrese la palabra: ")
        palabras.append(palabra)

def mayorA5():
    for i in range(len(palabras)):
        if len(palabras[i]) > 5:  
            mayoresA5.append(palabras[i])

# Bloque principal
cargarDatos()
mayorA5()

print("Las palabras con más de 5 letras son:")
for palabra in mayoresA5:
    print(palabra)

print("Cantidad de palabras con más de 5 letras:", len(mayoresA5))
