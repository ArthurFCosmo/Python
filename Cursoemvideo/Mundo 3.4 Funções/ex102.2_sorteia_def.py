from random import randint
def sorteia(lista):
    CONT = 0
    while CONT < 5:
        lista.append(randint(1, 10))
        CONT += 1
    print(f'Os valores sorteados foram: {lista}')
def somarpares():
    SOMA = 0
    for v in NUM:
        if v % 2 == 0:
            SOMA += v
    print(f'A soma dos números pares vale: {SOMA}')


NUM = list()
sorteia(NUM)
somarpares()
