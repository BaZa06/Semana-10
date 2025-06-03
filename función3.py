#Calcular el área de un circulo

"""Fórmula area = pi * (r * r)"""

#Nota: La función tiene que ser un verbo

def calcular_area_circulo(radio):
    pi = 3.1416
    return pi * (radio * radio)
radio = float(input("Ingrese el radio del circulo: "))
pi = 3.1416
calcular_area_circulo = pi * (radio * radio)

print(f"El área del criculo es {calcular_area_circulo:.2f} con un radio de {radio}")