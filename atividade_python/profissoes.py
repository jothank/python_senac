class Profissoes():

    def __init__(self, nome_empregado: str, salario: float, hora_por_dia: float) -> None:
        self.nome_empregado = nome_empregado
        self.salario = salario
        self.hora_por_dia = hora_por_dia
        self.cargo = None
        self.sexo = None
        self.hora_extra = 0
        self.salario_anual = 0
        self.bonificacao = 0

    def programa(self):
        self.nome_empregado = input('Digite o nome do empregador: ')
        self.salario_mensal = float(input('Digite Salario: '))         

    def horas_mes(self): 
        self.hora_por_dia = float(input('Digite quantidade de horas por dia 8, 6 ou 4: '))  
        if self.hora_por_dia == 8:
            self.quant_horas_mes = 220
            print(f'Horas mês será 220:00')
        elif self.hora_por_dia == 6:
            self.quant_horas_mes = 180
            print(f'Horas mês será 180:00')
        elif self.hora_por_dia == 4:
            self.quant_horas_mes = 120
            print(f'Horas mês será 120:00')
        else:
            print('Erro! digite a quantidade de horas dia correta')

    def sal_anual(self):
        self.salario_anual = self.salario_mensal*12
        print(f'O salário anual será R${self.salario_anual:.2f}')

    def quant_horas_anos(self):
        self.sexo = input('Digite seu sexo sendo M - Masculino ou F - Feminino: ')
        if self.sexo == 'M' or self.sexo == 'm':
            self.calcula_horas_anos_30 = (self.hora_por_dia*365)*30
            print(f'Quantidade de horas trabalhada quando possuir 30 anos será {self.calcula_horas_anos_30:.2f} horas, considerando {self.hora_por_dia:.2f} horas dia.')
        elif self.sexo == 'F' or self.sexo == 'f':
            self.calcula_horas_anos_25 = (self.hora_por_dia*365)*25        
            print(f'Quantidade de horas trabalhada quando possuir 25 anos será {self.calcula_horas_anos_25:.2f} horas, considerando {self.hora_por_dia:.2f} horas dia.')
        else:
            print('Erro! digite o sexo correto')     
 
'''
     def horas_extras_mes(self):
        self.quant_he = float(input("Digite a quantidade de horas extras mês: "))
        self.quant_he = self.quant_he*

    def aumento_salario(self):
        self.salario_aumento = (self.salario_mensal*0.10)+self.salario_mensal
        print(f'O salário do mês com aumento de 10% será {self.salario_aumento}')
'''
