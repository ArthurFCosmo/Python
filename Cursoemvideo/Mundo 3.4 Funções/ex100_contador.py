from time import sleep
def contador(I, F, P):
    if P < 0:
        print('-=' * 30)
        print(f'Contagem regressiva de {I} até {F} de {P} em {P}')
        for laco in range(I, F - 1, P):
            print(f'{laco}  ', end='', flush=True)
            sleep(0.5)
        print('Fim')
        print('-=' * 30)
    elif I > F:
        print('-=' * 30)
        print(f'Contagem regressiva de {I} até {F} de {P} em {P}')
        P = P * -1
        for laco in range(I, F - 1, P):
            print(f'{laco}  ', end='', flush=True)
            sleep(0.5)
        print('Fim')
        print('-=' * 30)
    elif P == 0:
        print('-=' * 30)
        print(f'Contagem regressiva de {I} até {F} de {P} em {1}')
        for laco in range(I, F + 1, 1):
            print(f'{laco}  ', end='', flush=True)
            sleep(0.5)
        print('Fim')
        print('-=' * 30)
    else:
        print('-=' * 30)
        print(f'Contagem regressiva de {I} até {F} de {P} em {P}')
        for laco in range(I, F + 1, P):
            print(f'{laco}  ', end='', flush=True)
            sleep(0.5)
        print('Fim')
        print('-=' * 30)



contador(0, 10, 1)
contador(10, 0, 1)

INICIO = int(input('Digite o número inicial da sua contagem: '))
FIM = int(input('Digite o número final da sua contagem: '))
PASSO = int(input('Digite de quanto em quanto sua contagem vai pular: '))

contador(INICIO, FIM, PASSO)
