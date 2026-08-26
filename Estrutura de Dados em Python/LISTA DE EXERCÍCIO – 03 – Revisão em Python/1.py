'''
Escreva um programa que recebe cinco notas de um aluno e calcula a média. Em seguida, exiba se o
aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).

'''
notas = []

print("Calcule sua média inserindo as 5 notas obtidas: ")

for i in range(5):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

total = sum(notas)
media = total / 5

if media >= 7:
    print("Aprovado com média" ,media)
elif media < 7:
    print("Reprovado com média" ,media)


