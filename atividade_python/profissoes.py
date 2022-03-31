class Profissoes():

    def __init__(self, nome_empregado: str, salario: float, hora_por_dia: float, cargo: str, sexo: str) -> None:
        self.nome_empregado = nome_empregado
        self.salario = salario
        self.hora_por_dia = hora_por_dia
        self.cargo = cargo
        self.sexo = sexo
        self.valor_horas_extras = 0
        self.valor_horas_falta = 0
        self.salario_anual = 0
        self.bonificacao = 0

    def nomeEmpregado(self):
        ##self.nome_empregado = input('Digite o nome do empregador: ')
        print(f'Nome do funcionario é {self.nome_empregado}')

    def salarioMensal(self):
        ##self.salario = float(input('Digite Salario R$'))
        print(f'Salário é R${self.salario}')

    def horas_faltas(self):
        self.valor_horas_falta = (self.salario/220)
        print(f'O valor de uma falta dia é R${self.valor_horas_falta:.2f}')

    def horas_extras(self):
        self.valor_horas_extras = (self.salario/220)*0.5+(self.salario/220)
        print(f'Ganhará R${self.valor_horas_extras:.2f} por horas em horas extras conforme salario mensal R${self.salario:.2f}')

    def selecionar_cargo_bonificacao(self):
        ##self.cargo = input('Selecione cargo 1 - Anestesista, 2 - Cirurgiao, 3 - Enfermeiro, 4 - Médico ou 5 - Recepcionista: ')
        if self.cargo == '1':
            self.bonificacao = self.salario*0.1
            print(f'Bonificação é 10% receberá como Anestesista é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario:.2f}')
        elif self.cargo == '2':
            self.bonificacao = self.salario*0.15
            print(f'Bonificação é 15% receberá como Cirurgiao é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario:.2f}')
        elif self.cargo == '3':
            self.bonificacao = self.salario*0.2
            print(f'Bonificação é 20% receberá como Enfermeiro é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario:.2f}')
        elif self.cargo == '4':
            self.bonificacao = self.salario*0.3
            print(f'Bonificação é 30% receberá como Médico é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario:.2f}')
        elif self.cargo == '5':
            self.bonificacao = self.salario*0.15
            print(f'Bonificação é 15% receberá como Recepcionista é R${self.bonificacao:.2f} conforme salario mensal de R${self.salario:.2f}')
        else:
            print('Erro! digite um numero de cargo correto')

    def horas_mes(self):
        ##self.hora_por_dia = float(input('Digite quantidade de horas por dia 8, 6 ou 4: '))
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
        self.salario_anual = self.salario*12
        print(f'O salário anual será R${self.salario_anual:.2f}')

    def quant_horas_anos(self):
        ##self.sexo = input('Digite seu sexo sendo M - Masculino ou F - Feminino: ')
        if self.sexo == 'M' or self.sexo == 'm':
            self.calcula_horas_anos_30 = (self.hora_por_dia*365)*30
            print(f'Quantidade de horas trabalhada quando possuir 30 anos será {self.calcula_horas_anos_30:.2f} horas, considerando {self.hora_por_dia:.2f} horas dia.')
        elif self.sexo == 'F' or self.sexo == 'f':
            self.calcula_horas_anos_25 = (self.hora_por_dia*365)*25
            print(f'Quantidade de horas trabalhada quando possuir 25 anos será {self.calcula_horas_anos_25:.2f} horas, considerando {self.hora_por_dia:.2f} horas dia.')
        else:
            print('Erro! digite o sexo correto')

    def exibir_cargo(self):
        if self.cargo == '1':
            print(f'Cargo do funcionario é Anestesista')
        elif self.cargo == '2':
            print(f'Cargo do funcionario é Cirurgiao')
        elif self.cargo == '3':
            print(f'Cargo do funcionario é Enfermeiro')
        elif self.cargo == '4':
            print(f'Cargo do funcionario é Médico')
        elif self.cargo == '5':
            print(f'Cargo do funcionario é Recepcionista')
        else:
            print('Erro! digite um numero de cargo correto')

    def horas_almoço(self):
        if self.hora_por_dia == 8:
            print(f'Funcionario terá direito a 01:00 hora de almoço')
        elif self.hora_por_dia == 6:
            print(f'Funcionario terá direito a 00:15 minutos de almoço')
        elif self.hora_por_dia == 4:
            print(f'Funcionario não terá direito a almoço')
        else:
            print('Erro! digite a quantidade de horas dia correta') 
            
