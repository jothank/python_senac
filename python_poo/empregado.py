class Empregado():

    def __init__(self, nome: str, sobre_nome: str, salario_mensal: float) -> None:
        self.salario_mensal = salario_mensal
        if salario_mensal < 0.0:
            self.salario = 0

        self.nome = nome
        self.sobre_nome = sobre_nome
        self.salario_anual = 0

    def programa(self):
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        self.salario_mensal = float(input("Digite Salario: "))

    def sal_anual(self):
        self.salario_anual = self.salario_mensal*12
        print(f"{self.salario_anual}")

    def aumento_salario(self):
        self.salario_anual 