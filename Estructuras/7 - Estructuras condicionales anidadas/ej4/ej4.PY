preg = int(input("cantidad de preguntas que se realizaron: "))
correctas = int (input("cantidad de preguntas que contestaron correctamente"))
porcentaje = (correctas * 100)/preg

if porcentaje >= 90:
    print("Usted tiene un nivel maximo de respuestas correctas")
else:
    if 75 <= porcentaje < 90:
        print("Usted tiene un nivel medio de respuestas correctas")
    elif 50 <= porcentaje < 75:
        print("Usted tiene un nivel regular de respuestas correctas")
    else: 
        print("Usted esta fuera de nivel")
        
print("El porcentaje es: ", porcentaje)
