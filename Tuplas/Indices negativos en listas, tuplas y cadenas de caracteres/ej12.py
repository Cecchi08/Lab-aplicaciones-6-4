def invertir_cadena():
    cadena = input("Ingrese una cadena de texto: ")

    print("Cadena invertida usando subíndices negativos:")
    for i in range(-1, -len(cadena)-1, -1):
        print(cadena[i], end="") 
    print()  

invertir_cadena()
