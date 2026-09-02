'''
8. Crie uma classe chamada "Aluno" com atributos "nome" e "notas". Implemente um método chamado
"calcular_media" que retorna a média das notas do aluno.
'''

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

nome = input("Digite o nome do aluno: ")
quantidade_notas = int(input("Quantas notas deseja informar? "))

notas = []
for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

aluno = Aluno(nome, notas)
print(f"A média de {aluno.nome} é {aluno.calcular_media():.2f}")
