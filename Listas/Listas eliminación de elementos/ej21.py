def gestionar_lista():
    lista = []

    for i in range(5):
        numero = int(input(f"Ingrese el número {i+1}: "))
        lista.append(numero)

    lista_mayor_10 = [num for num in lista if num >= 10]

    lista_sin_mayor_10 = [num for num in lista if num < 10]

    print("\nLista original:", lista)

    print("\nElementos mayores o iguales a 10:", lista_mayor_10)

    print("\nNueva lista sin los elementos mayores o iguales a 10:", lista_sin_mayor_10)

gestionar_lista()
