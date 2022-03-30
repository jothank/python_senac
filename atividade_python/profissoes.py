class Profissoes():

    def __init__(self, nome_empregado: str, salario: float, hora_por_dia: float) -> None:
        self.nome_empregado = nome_empregado
        self.salario = salario
        self.hora_por_dia = hora_por_dia
        self.cargo = str
        self.sexo = None
        self.hora_extra = 0
        self.salario_anual = 0
        self.bonificacao = 0

    def nomeEmpregado(self):
        self.nome_empregado = input('Digite o nome do empregador: ')         

    def salarioMensal(self):
        self.salario_mensal = float(input('Digite Salario R$')) 

    def horas_extras_mes(self):
        self.valor_horas_extras = (self.salario_mensal/220)*0.5+(self.salario_mensal/220)
        print(f'Você irá ganhar R${self.valor_horas_extras:.2f} por horas em horas extras conforme salario mensal R${self.salario_mensal:.2f}')  

    def selecionar_cargo_bonificacao(self):
        self.cargo = input('Selecione cargo 1 - Suporte, 2 - Professor, 3 - Programador, 4 - Gerente ou 5 - Analista: ')     
        if self.cargo == '1':
            self.bonificacao = self.salario_mensal*0.1
            print(f'Bonificação de 10% que você receberá como Suporte é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario_mensal:.2f}')
        elif self.cargo == '2':
            self.bonificacao = self.salario_mensal*0.15
            print(f'Bonificação de 15% que você receberá como Professor é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario_mensal:.2f}')
        elif self.cargo == '3':
            self.bonificacao = self.salario_mensal*0.2
            print(f'Bonificação de 20% que você receberá como Programador é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario_mensal:.2f}')
        elif self.cargo == '4':
            self.bonificacao = self.salario_mensal*0.3
            print(f'Bonificação de 30% que você receberá como Gerente é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario_mensal:.2f}')
        elif self.cargo == '5':
            self.bonificacao = self.salario_mensal*0.15
            print(f'Bonificação de 15% que você receberá como Analista é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario_mensal:.2f}')
        else:
            print('Erro! digite um numero de cargo correto')

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
 
