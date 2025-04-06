num = int(input("Ingrese un numero positivo "))

if num < 10:
    print("El numero tiene un digito")
elif 10 <= num <= 99:
    print("El numero tiene dos digitos")
elif num >= 100:
    print("El numero tiene tres digitos")
else:
    print("¡¡ERRORRRRR!!!!! BURRRO")
    