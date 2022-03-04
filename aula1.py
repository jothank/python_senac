saldo = int(input("Digite o saldo médio do último ano: "))

if saldo <=200:
    print("Sem crédito especial")
elif saldo <=400:
    cre_esp = (saldo*0.20)
    print(f"Seu saldo médio é {saldo} e voce tem direito à {cre_esp} de saldo especial")
elif saldo <=600:
    cre_esp = (saldo*0.30)
    print(f"Seu saldo médio é {saldo} e voce tem direito à {cre_esp} de saldo especial")
elif saldo >600:
    cre_esp = (saldo*0.40)
    print(f"Seu saldo médio é {saldo} e voce tem direito à {cre_esp} de saldo especial")
else:
    print("erro tente novamente!")
    


compra = input("Digite o código da compra: ")
quantidade = int(input("Digite a quantidade: "))

if compra == "100":
    valor = quantidade*1.20
elif compra == "101":
    valor = quantidade*1.30
elif compra == "102":
    valor = quantidade*1.50
elif compra == "103":
    valor = quantidade*1.20
elif compra == "104":
    valor = quantidade*1.30
elif compra == "105":
    valor = quantidade*1.00
else:
    print("Código inválido!")

print(f"O valor a ser pago é R${valor}")



altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo para Masculino = M ou Feminino = F: ")

if sexo == "M" or sexo =="m":
    print(f"{(72.7*altura)-58:.2f}")
elif sexo == "F" or sexo =="f":
    print(f"{(62.1*altura)-44.7:.2f}")
else:
    print("Digite um sexo valido!")



compra = int(input("Digite o código da compra: "))
quantidade = int(input("Digite a quantidade: "))

if compra == 100:
    print(f"O valor a ser pago é R${quantidade*1.20:.2f}")
elif compra == 101:
    print(f"O valor a ser pago é R${quantidade*1.30:.2f}")
elif compra == 102:
    print(f"O valor a ser pago é R${quantidade*1.50:.2f}")
elif compra == 103:
    print(f"O valor a ser pago é R${quantidade*1.20:.2f}")
elif compra == 104:
    print(f"O valor a ser pago é R${quantidade*1.30:.2f}")
elif compra == 105:
    print(f"O valor a ser pago é R${quantidade*1.00:.2f}")
else:
    print("Código inválido!")



numero = int(input("Digite um numero: "))

if (numero%2) == 0:
    print("Seu número é Par")
else:
    print("Seu número é Ímpar")
    
if numero>0:
    print("Seu número é Positivo")
else:
    print("Seu número é Negativo")



idade = int(input("Qual sua idade: "))

if idade >= 5 and idade <= 7:
    print("infantil A")
elif idade >= 8 and idade <= 10:
    print("infantil B")
elif idade >= 11 and idade <= 13:
    print("juvenil A")
elif idade >= 14 and idade <= 17:
    print("juvenil B")
elif idade >=18:
    print("audulto")
else:
    print("sem categoria")
    
