lista1 = 0
lista2 = 0
num1 = 0
num2 = 0

i = 0
while i < 15:
    num1 = int(input("Ingrese un numero "))
    lista1 += num1
    i += 1

i = 0 
while i < 15:
    num2 = int(input("Ingrese un numero "))
    lista2 += num2
    i += 1

if lista1 > lista2:
    print("Lista 1 mayor")
elif lista2 > lista1:
    print("Lista 2 mayor")
else:
    print("Listas iguales")