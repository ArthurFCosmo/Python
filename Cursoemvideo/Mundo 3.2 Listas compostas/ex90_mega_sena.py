# Pedir no input um número de palpites
# Mostrar uma listinha de 6 números (Sem repetições) para cada palpite que o input pediu

import random

LISTA = []
CONT = 0

palpites = int(input('Quantos palpites você quer? '))

while True:
    for pal in range(0, 6):
        num = random.randint(0, 99)

        if num in LISTA:
            num += 1
            LISTA.append(num)
            
        else:
            LISTA.append(num)
    
    print(LISTA)
    LISTA.clear()

    CONT += 1

    if CONT == palpites:
        break
