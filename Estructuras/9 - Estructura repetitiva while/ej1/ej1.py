cont_notas = 0
aprobados = 0
desaprobados = 0

while cont_notas < 9:
    cont_notas +=1
    nota = int(input("Ingrese la nota "))
    if nota >= 7:
        aprobados += 1
    else:
        desaprobados += 1

print("La cantidad de aprobados son: ", aprobados, ". Y la cantidad de desaproados son: ", desaprobados)