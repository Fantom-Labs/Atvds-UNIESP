'''
6. Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes
nela.
'''

def conta_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

texto = input("Digite uma frase ou palavra: ")

print(f"Quantidade de vogais: {conta_vogais(texto)}")
