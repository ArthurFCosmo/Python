from random import randint
def sorteia():
    LIST = [randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99)]
    LISTA.append(LIST[:])
    print(f'Os valores foram: {LIST}')
def soma():
    SOMA = 0
    for c in LISTA[0]:
        if c % 2 == 0:
            SOMA += c
    print(f'A soma dos valores pares vale: {SOMA}')

LISTA = []
sorteia()
soma()
