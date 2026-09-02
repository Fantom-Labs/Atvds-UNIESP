'''
10. Uma lista contém os valores: 1, 2, 3, 4, 5, 6.
Exclua os valores 3 e 5, um de cada vez, e mostre a lista após cada exclusão.
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


valores = ListaSequencial(6)
for v in [1, 2, 3, 4, 5, 6]:
    valores.inserir(v)

valores.excluir(3)
valores.imprimir()

valores.excluir(5)
valores.imprimir()
