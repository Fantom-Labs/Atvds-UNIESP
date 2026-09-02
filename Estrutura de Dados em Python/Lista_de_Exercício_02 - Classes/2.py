'''
2. Crie uma classe chamada "Livro" que tenha atributos "titulo" e "autor". Implemente um método
chamado "detalhes" que retorna uma string com as informações do livro.
'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo} | Autor: {self.autor}"

titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
livro = Livro(titulo, autor)
print(livro.detalhes())
