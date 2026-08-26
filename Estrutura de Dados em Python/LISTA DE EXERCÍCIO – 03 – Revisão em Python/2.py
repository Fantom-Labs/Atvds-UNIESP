'''
2. Escreva uma função que calcula o fatorial
de um número inteiro positivo fornecido pelo usuário.

'''
def fatorial(numero):
    resultado =  1
    for i in range(1, numero+1):
        resultado = (resultado * i)
    return resultado


numero= int(input("Digite um numero inteiro positivo: "))


print (fatorial(numero))