negativo = 0
positivo = 0
multiplo_15 = 0
suma_pares = 0
for i in range(11):
    valores = int(input("ingresar numeros: "))
    if valores < 0:
        negativo += 1
    else:
        positivo += 1
    if valores % 15 == 0:
        multiplo_15 += 1
    if valores % 2 == 0:
        suma_pares = suma_pares + valores
print("numeros negativos: ",negativo)
print("numeros positivos: ",positivo)
print("numeros multiplos de 15:",multiplo_15)
print("suma de numeros pares : ",suma_pares)