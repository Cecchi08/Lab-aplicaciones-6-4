lista = []
mayorYMenor = ()

def agregarValores():
    for i in range(5):
        variable = int(input("Ingrese un numero: "))
        lista.append(variable)

def menorYMayor():
    global mayorYMenor
    lista.sort()
    mayorYMenor = (lista[0], lista[-1])

agregarValores()
menorYMayor()
print("El menor es:", mayorYMenor[0])
print("El mayor es:", mayorYMenor[1])
