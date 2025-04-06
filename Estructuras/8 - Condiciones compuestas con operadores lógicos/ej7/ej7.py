num1 = int(input("Ingrese un numero "))
num2 = int(input("Ingrese un numero "))
num3 = int(input("Ingrese un numero "))

mayor = 0

if num1 > num2:
    if num1 > num3:
        mayor = num1
    else:
        mayor = num3
else:
    if num2 > num3:
        mayor = num2
    else:
        mayor = num3

print("El mayor de todos es: ", mayor)
menor = 0


if num1 < num2 and num1 < num3:
        menor = num1
else:
    if num2 < num3:
        menor = num2
    else:
        menor = num3



print("El menor de los tres es ", menor)