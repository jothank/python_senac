import funcao

calc_tabuada = int(input(
    "Digite um numero para tabuado por padrão é tabuadax10, caso não queria digite -1: "))
num_tabuada = int(input("Tabuada inicia em: "))
num_quantidade = int(input("Tabuada finaliza em: "))
resultado = funcao.tabuada(calc_tabuada, num_tabuada, num_quantidade)

salario_colab = float(input("Digite valor da venda: "))
resulta = funcao.salario_colaborador(salario_colab)

produto = float(input("Digite o preço: "))
resultado = funcao.produto(produto)

litro = int(input("Digite a quantidade de litros: "))
resultado = funcao.tonel(litro)

moeda1 = int(input("Digite quantidade moeda 1 centavo: "))
moeda5 = int(input("Digite quantidade moeda 5 centavos: "))
moeda10 = int(input("Digite quantidade moeda 10 centavos: "))
moeda25 = int(input("Digite quantidade moeda 25 centavos: "))
moeda50 = int(input("Digite quantidade moeda 50 centavos: "))
moeda1real = int(input("Digite quantidade moeda 1 real: "))
resultado = funcao.cofrinho(moeda1, moeda5, moeda10,
                            moeda25, moeda50, moeda1real)

coca_350 = float(input("Digite quantidade de coca 350 ml: "))
coca_600 = float(input("Digite quantidade de coca 600 ml: "))
coca_2000 = float(input("Digite quantidade de coca 2 litros: "))
resultado = funcao.coca_cola(coca_350, coca_600, coca_2000)

hor_normal = float(input("Digite quantidade de horas normais: "))
hor_extra = float(input("Digite quantidade de horas extras: "))
resultado = funcao.salario_bruto_liquido(hor_normal, hor_extra)

calc_celsius = float(input("Digiste temperatura em Celsius: "))
resultado = funcao.temp_celsius(calc_celsius)

salario = float(input("Digite salário: "))
resultado = funcao.somar_porcentagem(salario, 30)
