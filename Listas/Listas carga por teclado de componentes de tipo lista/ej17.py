def cargar_datos():
    paises = {}  
    for i in range(4):
        pais = input("Ingrese el nombre del país: ")
        temperaturas = []
        for mes in range(3):
            temperatura = float(input(f"Ingrese la temperatura media del mes {mes + 1} para {pais}: "))
            temperaturas.append(temperatura)
        paises[pais] = temperaturas
    return paises

def imprimir_temperaturas(paises):
    print("\nTemperaturas medias mensuales de los países:")
    for pais, temperaturas in paises.items():
        print(f"{pais}: {temperaturas}")

def calcular_temperatura_media(paises):
    temperaturas_trimestrales = {}
    for pais, temperaturas in paises.items():
        temperatura_media = sum(temperaturas) / len(temperaturas)
        temperaturas_trimestrales[pais] = temperatura_media
    return temperaturas_trimestrales

def imprimir_temperaturas_trimestrales(temperaturas_trimestrales):
    print("\nTemperaturas medias trimestrales de los países:")
    for pais, temperatura_media in temperaturas_trimestrales.items():
        print(f"{pais}: {temperatura_media:.2f}")

def pais_con_mayor_temperatura(temperaturas_trimestrales):
    pais_max_temp = max(temperaturas_trimestrales, key=temperaturas_trimestrales.get)
    return pais_max_temp, temperaturas_trimestrales[pais_max_temp]

def main():
    paises = cargar_datos()

    imprimir_temperaturas(paises)

    temperaturas_trimestrales = calcular_temperatura_media(paises)

    imprimir_temperaturas_trimestrales(temperaturas_trimestrales)
    
    pais_max_temp, temp_max = pais_con_mayor_temperatura(temperaturas_trimestrales)
    print(f"\nEl país con la temperatura media trimestral mayor es {pais_max_temp} con una temperatura de {temp_max:.2f}°C")

main()
