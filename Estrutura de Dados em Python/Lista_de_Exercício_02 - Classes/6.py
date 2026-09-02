'''
6. Crie uma classe chamada "Produto" com atributos "nome", "preco" e "quantidade". Implemente um
método chamado "calcular_total" que retorna o valor total do produto (preço * quantidade).
'''

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
produto = Produto(nome, preco, quantidade)
print(f"O valor total de {produto.nome} é R$ {produto.calcular_total():.2f}")
