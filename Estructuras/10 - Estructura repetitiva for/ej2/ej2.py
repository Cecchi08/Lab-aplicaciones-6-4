contador = 0
for i in range(10):
    num = int(input("Ingrese 10 numeros "))
    if i >= 5:
        contador += num
        
print("La suma es ", contador)