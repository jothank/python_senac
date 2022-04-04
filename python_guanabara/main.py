import random

while True:

    sorteio_numero1 = random.randint(1, 10)
    sorteio_numero2 = random.randint(1, 10)
    
    if sorteio_numero1 == sorteio_numero2:
        print(f'{sorteio_numero1} e {sorteio_numero2}')
        break
    else:
        print(f'{sorteio_numero1} e {sorteio_numero2}')
