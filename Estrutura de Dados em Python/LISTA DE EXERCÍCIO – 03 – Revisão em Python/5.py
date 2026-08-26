'''
5. Crie uma função que verifica se um número é primo ou não.

'''

def eh_primo(num):
    if num < 2:
        return False

    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False

    return primo

num = int(input("Digite um número: "))

if eh_primo(num):
    print("é primo")
else:
    print("Não é primo")
