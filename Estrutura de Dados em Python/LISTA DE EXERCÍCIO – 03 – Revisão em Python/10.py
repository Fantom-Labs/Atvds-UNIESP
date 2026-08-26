'''
10. Escreva uma função que gera a sequência de Fibonacci até um determinado número de termos
especificado pelo usuário.
'''

def fibonacci(n_termos):
    sequencia = []
    a, b = 0, 1
    for _ in range(n_termos):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

n_termos = int(input("Quantos termos da sequencia de Fibonacci você quer gerar? "))

print(fibonacci(n_termos))
