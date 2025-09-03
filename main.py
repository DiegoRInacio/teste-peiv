class Pessoa:
    def __init__(self, nome=None, idade=None, altura=None):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    @classmethod
    def cadastro(cls):
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        altura = float(input("Digite sua altura: "))

        return cls(nome, idade, altura)  # Retorna a nova instância
