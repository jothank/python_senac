soma=0
quantidade=0
negativo=0 
positivo=0 

while True:
    n = float(input("Digite nota: "))
    if n == 0:
        break
    quantidade += 1 
    soma += n
    
    if n > 0:
        positivo +=1
        
    if n < 0:
        negativo +=1
        
print(f"\nMédia aritmética é: {soma/quantidade:.2f}")
print(f"Quantidade de numeros positivos são: {positivo:.0f}")
print(f"Quantidade de numeros negativos são: {negativo:.0f}")
print(f"Porcentagem de positivos são: {(positivo/quantidade)*100}%")
print(f"Porcentagem de negativos são: {(negativo/quantidade)*100}%")


alt_maior = 0 
alt_menor = 999
quantidade = 0
media = 0

for x in range(0,15):
    altura = float(input("Digite sua altura: "))
    if altura < 0:
        break
    quantidade +=1 
    media += altura
    
    if (altura > alt_maior):
        alt_maior = altura
        
    if (altura < alt_menor):
        alt_menor = altura

print(f"A altura maior foi: {alt_maior:.2f}")
print(f"A altura menor foi: {alt_menor:.2f}").
print(f"A média das alturas foram: {media/altura:.2f}")


soma = 0
conta = 0 

for n in range(1,501,2):
    if n % 3 == 0:
        soma += n
        conta += 1
        
print(f"Os numeros são {conta} e a soma é {soma}")


num2 = num1 = 1
resultado = 0

for i in range(50):
   resultado += num2 / num1
   num2 += 2
   num1 += 1
print(resultado)


n = int(input("Informe numero para tabuada: "))
i = 0

while i < 11:
    print(f"{n} x {i} = {n * i}")
    i += 1

i=0

while i < 10: 
    i += 1
    print(i) 
    if i == 7: 
        break

c1 = 0
c2 = 0
c3 = 0
c4 = 0

while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    if n >= 0 and n <= 25:
        c1 += 1
    elif n >= 26 and n <= 50:
        c2 += 1
    elif n >= 51 and n <= 75:
        c3 += 1
    elif n >= 76 and n <= 100:
        c4 += 1
    else:
        print("Número errado")
    
print(f"\nA quantidade de números entre  0 e 25  é: {c1}")
print(f"A quantidade de números entre 26 e 50  é: {c2}")
print(f"A quantidade de números entre 51 e 75  é: {c3}")
print(f"A quantidade de números entre 76 e 100 é: {c4}")


quant_sal=0
sal_soma=0
sal_maior=0
quant_fil=0
fil_soma=0
quant_pess=0

while True:
    salario = float(input("Digite seu salário: "))
    if salario < 0.1:
        break
    quant_sal += 1 
    sal_soma += salario
    
    filhos = int(input("Digite quantidade de filhos: "))
    quant_fil += 1 
    fil_soma += filhos
    
    if (salario>sal_maior):
        sal_maior = salario
        
    if (salario<=100):
        quant_pess += 1
        
print(f"\nMédia de salario é R${sal_soma/quant_sal:.2f}")
print(f"Média de filhos são {fil_soma/quant_fil:.2f}")
print(f"Salário maior foi R${sal_maior:.2f}")
print(f"Quantidade de pessoas com salário menor à R$100 são: {quant_pess}")


maior = 0 

while True:
    n = int(input("Digite um numero: "))
    if n == -1:
        break
    if (n > maior):
        maior = n

print(f"O número digitado maior é {maior}.")


quantidade = 0 

while True:
    n = int(input("Digite um numero: "))
    if n == 0:
        break
    if n >= 100 and n <= 200:
        quantidade += 1
        
print(f"Quantidade de numeros entre 100 e 200 foram {quantidade}.")


negativo = 0

for x in range(0,10):
    voto = int(input("Digite um numero inteiro: "))
    if (voto<0):
        negativo += voto

print(f"Soma dos negativos deu {negativo}")


quantidade = 0 
positivo = 0 
negativo = 0 
soma=0

while True:
    n = int(input("Digite um numero: "))
    if n == 0:
        break
    quantidade += 1 
    soma += n
    if n > 0:
        positivo +=1
    else:
        negativo +=1
        
if quantidade != 0:
    print(f"\nMédia é {soma/quantidade}")
print(f"Positivo foram {positivo}")
print(f"Negativo foram {negativo}")


chico = 1.50
juca = 1.10
ano = 0

while chico > juca:
    chico += 0.02
    juca += 0.03
    ano += 1 

print(f"Será necessário {ano} anos para jucas ser maior que chico")
  

candidato1= 0 
candidato2= 0 
candidato3= 0 
candidato4= 0 
nulos = 0
brancos = 0

for x in range(0,5):
    voto = input("Qual o seu voto: ")
    if voto == "1":
        candidato1 += 1
    elif voto == "2":
        candidato2 += 1
    elif voto == "3":
        candidato3 += 1
    elif voto == "4":
        candidato4 += 1
    elif voto == "5":
        nulos += 1
    elif voto == "6":
        brancos += 1 
    else:
        print("Voto invalido")
        continue

print(f"candidato1 recebeu {candidato1}")
print(f"candidato2 recebeu {candidato2}")
print(f"candidato3 recebeu {candidato3}")
print(f"candidato4 recebeu {candidato4}")
print(f"nulos recebeu {nulos}")
print(f"brancos recebeu {brancos}")
