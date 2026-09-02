'''
10. Crie uma classe chamada "Funcionario" com atributos "nome", "salario" e "cargo". Implemente um
método chamado "aumentar_salario" que recebe um valor percentual de aumento e atualiza o salário
do funcionário.
'''

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)
        print(f"Novo salário de {self.nome}: R$ {self.salario:.2f}")

nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
cargo = input("Digite o cargo do funcionário: ")
funcionario = Funcionario(nome, salario, cargo)

percentual = float(input("Digite o percentual de aumento: "))
funcionario.aumentar_salario(percentual)
