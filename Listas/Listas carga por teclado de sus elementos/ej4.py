sueldos = [45000.50, 38000.75, 52000.00, 47000.25, 41000.00]

print("Sueldos de los operarios:")
for sueldo in sueldos:
    print(f"${sueldo:.2f}")

promedio = sum(sueldos) / len(sueldos)

print(f"\nPromedio de sueldos: ${promedio:.2f}")
