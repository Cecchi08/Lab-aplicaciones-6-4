def procesar_cadena():
    cadena = input("Ingrese una cadena de texto: ")

    if len(cadena) < 2:
        print("La cadena debe tener al menos 2 caracteres.")
        return

    print("Primeros dos caracteres:", cadena[:2])
    print("Últimos dos caracteres:", cadena[-2:])
    print("Todos menos el primero y el último:", cadena[1:-1])

procesar_cadena()
