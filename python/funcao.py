def somar_porcentagem(valor: float, porc: float):
    resultado = valor+(valor*porc/100)
    print("Seu salário é de: ", resultado)


def temp_celsius(celsius: float):
    resultado = celsius*1.8+32
    print(resultado)


def salario_bruto_liquido(hora_normal: float, hora_extra: float):
    salario_bruto = hora_normal*10+hora_extra*15
    salario_liquido = salario_bruto-(salario_bruto*0.10)
    print(salario_bruto)
    print(salario_liquido)


def coca_cola(coca350: float, coca600: float, coca2000: float):
    total_litro = (coca350*350+coca600*600+coca2000*2000)/1000
    print("Total de litros", total_litro, "litros")


def cofrinho(m1: int, m5: int, m10: int, m25: int, m50: int, m1real: int):
    valor = ((m1*1+m5*5+m10*10+m25*25+m50*50)+m1real*100)/100
    print("Total do cofrinho é:", valor)


def tonel(litros: int):
    agua = litros*0.8
    maracuja = litros*0.2
    print("quantidade de litros é: ", litros, "litros")
    print("quantidade de agua que precisa é: ", agua, "litros")
    print("quantidade de suco de maracuja que precisa é: ", maracuja, "litros")
