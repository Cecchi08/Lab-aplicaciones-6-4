num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese un numero:"))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2
if num1 > num2:
    print("La suma es: ", suma)
    print("La resta es: ", resta)
elif num2 > num1:
    print("El producto es: ", producto)
    print("La division es: ", division)