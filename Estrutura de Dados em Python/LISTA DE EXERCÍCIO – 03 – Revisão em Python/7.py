'''
7. Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura
e peso.
'''

def calcula_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

print(f"Seu IMC é: {calcula_imc(peso, altura):.2f}")
