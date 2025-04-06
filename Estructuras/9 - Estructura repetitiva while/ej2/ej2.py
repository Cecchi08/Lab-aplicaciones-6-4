n = int(input("Ingrese el valor de n "))
promedio = 0
i = 0
while i < n:
    altura = int(input("Ingrese el valor de la altura "))
    promedio += altura
    i +=1
    

promedio /= n
print("El promedio de las alturas es ", promedio)