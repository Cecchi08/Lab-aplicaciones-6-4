x = 0
y = 0
valores = int(input("Ingrese la canitdad de valores "))
for i in range(valores):
    x = int(input("Ingrese x "))
    y = int(input("Ingrese y "))
    if x > 0 and y > 0:
        print("1° cuadrante")
    elif x < 0 and y > 0:
        print("2° cuadrante")
    elif x < 0 and y < 0:
        print("3° cuadrante")
    elif x > 0 and y < 0:
        print("4° cuadrante")