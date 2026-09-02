'''
3. Considere que foram cadastrados os clientes com os códigos 11, 22, 33, 44, 55.
Pesquise se o cliente com código 33 está presente e informe sua posição na lista.
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


clientes = ListaSequencial(5)
clientes.inserir(11)
clientes.inserir(22)
clientes.inserir(33)
clientes.inserir(44)
clientes.inserir(55)

posicao = clientes.pesquisar(33)
if posicao != -1:
    print(f"Cliente 33 encontrado na posição {posicao}.")
else:
    print("Cliente 33 não encontrado.")
