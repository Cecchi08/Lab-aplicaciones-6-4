num =int(input("Ingrese un numero del 1 al 10 "))
for i in range(13):
    if i == 0:
        i +=1
    else:
        print(i * num)
