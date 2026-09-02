'''
7. Crie uma classe chamada "Carro" com atributos "marca", "modelo" e "ano". Implemente um método
chamado "detalhes" que retorna uma string com as informações do carro.
'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}"

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = int(input("Digite o ano do carro: "))
carro = Carro(marca, modelo, ano)
print(carro.detalhes())
