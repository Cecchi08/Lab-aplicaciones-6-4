n = int(input("Ingrese el valor de n "))
pares = 0
impares = 0
i = 1
while i <= n:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1 

print("La cantidad de numeros pares es ", pares)
print("La cantidad de numeros impares es ", impares)