hom1 = int(input("Digite idade do homem: "))
hom2 = int(input("Digite idade do homem: "))
mul1 = int(input("Digite idade do mulher: "))
mul2  = int(input("Digite idade do mulher: "))

if hom1>hom2:
    if mul1>mul2:
        soma = hom2+mul1
        print(f"soma é {soma} e produto {hom1} {mul2}")
    else:
        soma = hom1+mul2
        print(f"soma é {soma} e produto {hom2} {mul1}")
elif hom2>hom1:
    if mul2>mul1:
        soma = hom1+mul2
        print(f"soma é {soma} e produto {hom2} {mul1}")
    else:
        soma = hom2+mul1
        print(f"soma é {soma} e produto {hom1} {mul2}")
else:
    print("erro")


ano_nasc = int(input("Digite ano de nascimento: "))
idade = 2022-ano_nasc

if idade >=16:
    print("Você pode votar")
else:
    print("Você não pode votar")



maca = float(input("Digite a quantidade de maçãs: "))

if maca < 12:
    valor = maca*1.30
    print(f"valor a pagar será {valor}")
else:
    valor = maca*1.00
    print(f"valor a pagar será {valor}")
    

valido = int(input("Digite a quantidade votos valido: "))
branco = int(input("Digite a quantidade votos brancos: "))
nulo = int(input("Digite a quantidade votos nulos: "))
eleitores = valido+branco+nulo

print(f"Quantidade de eleitores foi {eleitores}")
print(f"Votos validos foram {valido} percentual de {(valido/eleitores)*100}%")
print(f"Votos brancos foram {branco} percentual de {(branco/eleitores)*100}%")
print(f"Votos nulos foram {nulo} percentual de {(nulo/eleitores)*100}%")



a = False
b = True
c = False
x = 1.5
y = 3.2
x = x + 1
if (c == True or ( (x+y > 5) and (a == True and b == True) )):
    z = 0
else:
    z = 1
print(z)


tipo = input("Digite tipo do combustivel 1-Gasolina ou 2-Alcool: ")
litro = float(input("Digite a quantidade de litros: "))

if tipo == "1":
    if litro <= 20:
        valor = (litro*2.99)
        pagar = (valor*0.04)+valor
    else:
        valor = (litro*2.99)
        pagar = (valor*0.06)+valor
elif tipo == "2":
    if litro <= 20:
        valor = (litro*2.19)
        pagar = (valor*0.04)+valor
    else:
        valor = (litro*2.19)
        pagar = (valor*0.06)+valor
else:
    print("erro")

print(f"Valor a pagar é {pagar}")


n= int(input("Digite um numero de 1 à 3: ")) 
num1= int(input("Digite um numero: "))
num2= int(input("Digite outro numero: "))
num3= int(input("Digite ultimo numero: "))

if n == 1 and num1 > num2 and num2 > num3:
    print(num3, num2, num1)
elif n == 1 and num1 > num2 and num3 > num2:
    print(num2, num3, num1)
elif n == 1 and num2 > num3 and num3 > num1:
    print(num1, num3, num2)
elif n == 1 and num2 > num3 and num1 > num3:
    print(num3, num1, num2)
elif n == 1 and num3 > num2 and num2 > num1:
    print(num1, num2, num3)
elif n == 1 and num3 > num2 and num1 > num2:
    print(num2, num1, num3)
elif n == 2 and num1 > num2 and num2 > num3:
    print(num1, num2, num3)
elif n == 2 and num1 > num2 and num3 > num2:
    print(num1, num3, num2)
elif n == 2 and num2 > num3 and num3 > num1:
    print(num2, num3, num1)
elif n == 2 and num2 > num3 and num1 > num3:
    print(num2, num1, num3)
elif n == 2 and num3 > num2 and num2 > num1:
    print(num3, num2, num1)
elif n == 2 and num3 > num2 and num1 > num2:
    print(num3, num1, num2)
elif n == 3 and num1 > num2 and num2 > num3:
    print(num2, num1, num3)
elif n == 3 and num1 > num2 and num3 > num2:
    print(num3, num1, num2)
elif n == 3 and num2 > num3 and num3 > num1:
    print(num3, num2, num1)
elif n == 3 and num2 > num3 and num1 > num3:
    print(num1, num2, num3)
elif n == 3 and num3 > num2 and num2 > num1:
    print(num2, num3, num1)
elif n == 3 and num3 > num2 and num1 > num2:
    print(num1, num3, num2)
else:
    print("Digite um numero valido!")


numero = int(input("Digite um numero: "))

if numero == 0:
     print("Seu número é Zero")
elif numero > 0:
    print("Seu número é Positivo")
else:
    print("Seu número é Negativo")


num1= int(input("Digite um numero "))
num2= int(input("Digite outro numero "))

if (num1%2) ==0 and (num2%2) == 0:
    print("Seus numeros são multiplos")
else:
    print("Seus numeros não são multiplos")


num_aluno=input('Digite o numero do aluno: ')
num1=float(input('Digite um primeiro número: ')) 
num2=float(input('Digite um segundo número: ')) 
num3=float(input('Digite um terceiro número: '))
num4=float(input('Digite um quarto número: '))
med_exe= (num1+(num2*2)+(num3*3)+num4)/7

if med_exe < 4.0:
    resultado = "E"
    print(f"Número do aluno é {num_aluno}, a média dos exercícios é {num4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi reprovado")
elif med_exe >= 4.0 and med_exe < 6.0:
    resultado = "D"
    print(f"Número do aluno é {num_aluno}, a média dos exercícios é {num4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi reprovado")
elif med_exe >= 6.0 and med_exe < 7.5:
    resultado = "C"
    print(f"Número do aluno é {num_aluno}, a média dos exercícios é {num4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi aprovado")
elif med_exe  >=7.5 and med_exe < 9.0:
    resultado = "B"
    print(f"Número do aluno é {num_aluno}, a média dos exercícios é {num4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi aprovado")
elif med_exe >= 9.0:
    resultado = "A"
    print(f"Número do aluno é {num_aluno}, a média dos exercícios é {num4:.2f}, média de aproveitamento é {med_exe:.2f}, você foi aprovado")


num1=float(input('Digite um primeiro número: ')) 
num2=float(input('Digite um segundo número: ')) 
num3=float(input('Digite um terceiro número: '))
opcao=input("Digite 1-aritmética 2-ponderada ou 3-harmônica para escolher o calculo da média: ")

if opcao == "1":
    print((num1 + num2 + num3) / 3)
elif opcao == "2":
    print((num1*5 + num2*3 + num3*2) / 10)
elif opcao == "3":
    print((1/num1 + 1/num2 + 1/num3)/3)
else:
    print("Opção inválida!")


