sueldo = int(input("Ingrese su sueldo "))
anios = int(input("Ingrese sus años de antiguedad "))
aumento = 0
nuevo_sueldo = sueldo
if sueldo < 500 and anios >= 10:
    aumento = 20
    nuevo_sueldo += (aumento * sueldo) / 100
    print("Su sueldo ahora sera de: ", nuevo_sueldo)
elif sueldo < 500 and anios < 10:
    aumento = 5
    nuevo_sueldo += (aumento * sueldo) / 100
    print("Su sueldo ahora sera de: ", nuevo_sueldo)
elif sueldo >= 500:
    print("Usted seguira cobrando lo mismo, por pobre")