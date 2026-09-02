'''
5. Crie uma classe chamada "Pessoa" com atributos "nome" e "idade". Implemente um método
chamado "falar" que imprime uma mensagem com o nome da pessoa.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
pessoa = Pessoa(nome, idade)
pessoa.falar()
