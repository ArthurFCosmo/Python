def fatorial(F, SHOW=False):
    SOMA = 1
    for laco in range(F, 0, -1):
        SOMA *= laco
        if SHOW and laco != F:
            print(f'{F} x {laco} = {SOMA}')
    return SOMA

FATORIAL = int(input('Insira o número: '))
S = input('Deseja mostrar as mutiplicações [S//N]? ').upper()[0]
if S == 'S':
    S = True
else:
    S = False
print(fatorial(FATORIAL, S))
