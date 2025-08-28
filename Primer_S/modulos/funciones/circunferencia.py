import math
# Definir 3 funciones... Cálculo de perímetro, área y volumen...
pi = math.pi
def perimetro_circunferencia(radio):
    return radio * pi * 2

def area_circunferencia(radio):
    return pi * radio ** 2

def volumen_circunferencia(radio):
    return 4/3 * pi * radio ** 3