class Pessoas():
    def __init__(self, nome: str, idade: int, data_nascimento: str) -> None:
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.salario = 0
        self.cor_cabelo = None
        self.altura = None

    def andar(self):
        print(f"{self.nome} você está andando.")
