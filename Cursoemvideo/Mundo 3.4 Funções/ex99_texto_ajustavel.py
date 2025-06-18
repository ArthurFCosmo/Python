# escreva um programa que ajuste o cabeçalho com o tamanho do texto através de uma função
def titulo(txt):
    if len(txt) % 2 == 0:
        TAM = int(len(txt) * 2)
        print('-' * TAM )
        print(f'{txt:^{TAM}}')
        print('-' * TAM)
    else:
        TAM = int(len(txt) * 2 + 1)
        print('-' * TAM)
        print(f'{txt:^{TAM}}')
        print('-' * TAM)


TEXTO = str(input('Digite aqui o texto: '))
print(len(TEXTO))
titulo(TEXTO)
