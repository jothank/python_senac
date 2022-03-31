import profissoes


class Cirurgiao(profissoes.Profissoes):
    def __init__(self, nome_empregado, salario, hora_por_dia, cargo, sexo):
        super().__init__(nome_empregado, salario, hora_por_dia, cargo, sexo)
