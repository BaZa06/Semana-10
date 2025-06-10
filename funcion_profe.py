


import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def main():
    radio = float(input("Ingrese el radio del ciruclo: "))
    area = calcular_area_circulo(radio)
    print(f"El área del circulo con un radio de {radio} es {area:.2f}")

main()   