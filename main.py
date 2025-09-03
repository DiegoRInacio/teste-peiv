class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.altura = None
    
    @classmethod
    def cadastro(cls):
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        altura = float(input("Digite sua altura: "))

        cls(nome, idade, altura)
        
