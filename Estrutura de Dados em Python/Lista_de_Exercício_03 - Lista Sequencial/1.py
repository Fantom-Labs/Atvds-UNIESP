'''
1. Crie uma lista sequencial com capacidade para 5 elementos. Insira as matrículas dos seguintes alunos:
101, 102, 103, 104.
Depois, imprima a lista para verificar os valores armazenados.
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


matriculas = ListaSequencial(5)
matriculas.inserir(101)
matriculas.inserir(102)
matriculas.inserir(103)
matriculas.inserir(104)
matriculas.imprimir()
