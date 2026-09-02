'''
8. Em um estacionamento cabem 4 carros. Insira as placas (numéricas fictícias): 1234, 5678, 9101,
1213.
Verifique se a placa 5678 está estacionada.
Depois, tente inserir a placa 1415. O que acontece?
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


estacionamento = ListaSequencial(4)
estacionamento.inserir(1234)
estacionamento.inserir(5678)
estacionamento.inserir(9101)
estacionamento.inserir(1213)

posicao = estacionamento.pesquisar(5678)
if posicao != -1:
    print(f"Placa 5678 está estacionada na posição {posicao}.")
else:
    print("Placa 5678 não está estacionada.")

# O estacionamento já está cheio (capacidade 4), então a inserção abaixo falha
estacionamento.inserir(1415)
