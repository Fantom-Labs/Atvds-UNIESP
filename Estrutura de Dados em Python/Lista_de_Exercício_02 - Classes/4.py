'''
4. Crie uma classe chamada "ContaBancaria" que tenha atributos "saldo" e "titular". Implemente
métodos "depositar" e "sacar" para manipular o saldo.
'''

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor:.2f} realizado. Saldo atual: {self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            print(f"Saque de {valor:.2f} realizado. Saldo atual: {self.saldo:.2f}")

titular = input("Digite o nome do titular: ")
conta = ContaBancaria(titular)

print("1 - Depositar")
print("2 - Sacar")
opcao = input("Escolha uma opção: ")

valor = float(input("Digite o valor: "))

if opcao == "1":
    conta.depositar(valor)
elif opcao == "2":
    conta.sacar(valor)
else:
    print("Opção inválida")
