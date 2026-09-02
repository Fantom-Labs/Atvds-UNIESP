'''
5. Pacientes aguardam atendimento e foram cadastrados os números de senha: 5, 6, 7, 8, 9.
Um paciente desistiu (senha 7).
Faça a exclusão deste paciente e imprima novamente a lista.
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


senhas = ListaSequencial(5)
senhas.inserir(5)
senhas.inserir(6)
senhas.inserir(7)
senhas.inserir(8)
senhas.inserir(9)

senhas.excluir(7)
senhas.imprimir()
