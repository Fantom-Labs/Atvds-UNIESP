'''
2. Uma loja deseja registrar os códigos dos produtos em estoque. Insira os códigos 45, 33, 27, 89,
56 em uma lista sequencial de capacidade 5.
Depois, tente inserir o produto 72 e observe o que acontece.
'''

class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.tamanho = 0
        self.vetor = [None] * capacidade

    def esta_cheia(self):
        return self.tamanho == self.capacidade

    def inserir(self, valor):
        if self.esta_cheia():
            print(f"Lista cheia! Não foi possível inserir o valor {valor}.")
            return False
        self.vetor[self.tamanho] = valor
        self.tamanho += 1
        print(f"Valor {valor} inserido com sucesso.")
        return True

    def pesquisar(self, valor):
        for posicao in range(self.tamanho):
            if self.vetor[posicao] == valor:
                return posicao
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            print(f"Valor {valor} não encontrado na lista.")
            return False
        for i in range(posicao, self.tamanho - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.vetor[self.tamanho - 1] = None
        self.tamanho -= 1
        print(f"Valor {valor} excluído com sucesso.")
        return True

    def imprimir(self):
        print("Lista:", self.vetor[:self.tamanho])


produtos = ListaSequencial(5)
produtos.inserir(45)
produtos.inserir(33)
produtos.inserir(27)
produtos.inserir(89)
produtos.inserir(56)
produtos.imprimir()

# A lista já está cheia (capacidade 5), então a inserção abaixo falha
produtos.inserir(72)
