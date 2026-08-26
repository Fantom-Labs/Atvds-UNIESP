'''
4. Escreva um programa que recebe um número inteiro
positivo e calcula a soma de seus dígitos.
'''

numero = int(input("Digite um número inteiro positivo: "))

numero_texto = str(numero)

soma = 0
for digito in numero_texto:
    soma = soma + int(digito)

print(soma)
