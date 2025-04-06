contador = 0
n = int(input("Ingrese el valor de n "))
for i in range(n):
    base = int(input("Ingrese la base "))
    altura = int(input("Ingrese la altura "))
    superficie = (base * altura) / 2
    print("La base es ", base, " La altura es ", altura, " Y la superficie es ", superficie)
    if superficie > 12:
        contador +=1

print("La cantidad de triangulos que su superficie supera los 12 son: ", contador)