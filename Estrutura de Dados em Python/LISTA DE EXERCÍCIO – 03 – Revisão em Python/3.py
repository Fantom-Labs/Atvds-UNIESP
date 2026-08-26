'''
3. Crie uma função que verifica se uma palavra ou frase
é um palíndromo (lê-se igual de trás para frente,
'''

def palindromo(palavra):
    palavra_limpa = palavra.lower().replace(" ", "")
    if palavra_limpa == palavra_limpa[::-1]:
        print("Palindromo")
    else:
        print("Não é")

palavra = input("Digite uma palavra ou frase pra verificar se é um palíndromo: ")

palindromo(palavra)