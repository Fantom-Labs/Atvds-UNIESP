'''
9. Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base
na escolha do usuário.
'''

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = input("Escolha uma operação: ")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if opcao == "1":
    print(soma(a, b))
elif opcao == "2":
    print(subtracao(a, b))
elif opcao == "3":
    print(multiplicacao(a, b))
elif opcao == "4":
    if b == 0:
        print("Não é possível dividir por zero")
    else:
        print(divisao(a, b))
else:
    print("Opção inválida")
