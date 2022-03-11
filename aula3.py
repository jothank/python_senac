negativos = []
cont = 0 
for n in range(0,5):
    numero = int(input("Informe um numero"))
    if numero <0:
        cont = cont + 1 
        negativos.append(numero)
print(cont)        


a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[]

for x in a:
    for y in b:
        c.append(x*y)
print(c)


numero = int(input("Fatorial de: ") )
resultado=1

for n in range(1,numero+1):
    resultado = resultado * n

print(resultado)


for x in range (101, 201, 2):
    print(x)


soma = 10
for x in range(1,501):
    soma = soma + x
    print(soma)


import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([21,22,23,24,25,26,27,28,29,30])
soma = x * y

print(soma)


i = range(1, 21)
x = list(i)
print(x)

i = reversed(range(1, 21))
x = list(i)
print(x)

for i in range(0,10):
    if i % 2 == 0:
        print(i)

for i in range(2,10,2):
    print(i)