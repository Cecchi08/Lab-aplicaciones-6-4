lista = []
mayorYMenor = []

def agregarValores():
    for i in range(5):
        variable = int(input("Ingrese un numero: "))
        lista.append(variable)

def menorYMayor():
    lista.sort()
    mayorYMenor.append(lista[0])  
    mayorYMenor.append(lista[-1])

agregarValores()
menorYMayor()
print("El menor es:", mayorYMenor[0])
print("El mayor es:", mayorYMenor[1])
