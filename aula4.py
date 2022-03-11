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
