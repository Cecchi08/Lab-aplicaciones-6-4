triangulos = int(input("Ingrese la cantidad de triangulos "))
escaleno = 0
isosceles = 0
equilatero = 0
for i in range(triangulos):
    lado1 = int(input("Ingrese el lado 1 "))
    lado2 = int(input("Ingrese el lado 2 "))
    lado3 = int(input("Ingrese el lado 3 "))
    if lado1 == lado2 == lado3:
        equilatero += 1
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado1 == lado3 != lado2:
        isosceles += 1
    else:
        escaleno += 1

print("La cantidad de triangulos equilatero ", equilatero)
print("La cantidad de triangulos isosceles ", isosceles)
print("La cantidad de triangulos escaleno ", escaleno)