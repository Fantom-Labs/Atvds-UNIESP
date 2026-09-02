'''
1. Crie uma classe chamada "Circulo" que tenha um atributo "raio". Implemente um método chamado
"calcular_area" que retorna a área do círculo.
'''

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
print(f"A área do círculo é {circulo.calcular_area():.2f}")
