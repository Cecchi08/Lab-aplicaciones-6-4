n = int(input("Ingrese el valor de n "))
sueldo = 0
gasto = 0
i = 0
sueldo_minimo = 0
sueldo_maximo = 0

while i < n:
    sueldo = int(input("Ingrese su sueldo "))
    if sueldo >= 100 and sueldo <= 300:
        sueldo_minimo += 1
        gasto += sueldo
    elif sueldo >= 300:
        sueldo_maximo += 1
        gasto += sueldo
    i += 1

print("La cantidad de personas que cobran entre 100 y 300 pesos son: ", sueldo_minimo)
print("La cantidad de personas que cobran mas de 300 pesos son: ", sueldo_maximo)
print("El gasto total de la empresa es de: ", gasto)