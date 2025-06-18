# Crie um programa que leia nome, sexo e idade de várias pessoas
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. no final mostre:
# quantas pessoas foram cadastradas
# a média de idade do grupo
# uma lista com todas as mulheres
# uma lista com todas as pessoas com idade acima da média

LISTA = []
DICT = {}

while True:
    DICT['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        SEXO = str(input('Sexo [M//F]: ')).upper()[0]
        if SEXO in 'MF':
            DICT['Sexo'] = SEXO
            break
        else:
            print('Erro! Digite apenas M ou F.')
    
    DICT['Idade'] = int(input('Idade: '))

    LISTA.append(DICT.copy())

    CONTINUAR = str(input('Quer continuar [S//N]? ')).upper()[0]
    if CONTINUAR == 'N':
        break
    elif CONTINUAR not in 'SN':
        print('Digite apenas [S] ou [N] !')

print()
print('=-=' * 30)
print()

print(f'Ao todo temos {len(LISTA)} pessoas cadastradas')

SOMA = 0
for c in range(0, len(LISTA)):
    SOMA += int(LISTA[c]['Idade'])

MEDIA = SOMA / len(LISTA)

print(f'A média das idades é {MEDIA} anos.')

print('As mulheres cadastradas foram: ', end='')

for c in range(0, len(LISTA)):
    if LISTA[c]['Sexo'] == 'F':
        print(f'{LISTA[c]["Nome"]}', end=', ')
print()

print('As pessoas com idade acima da média são: ', end='')

for c in range(0, len(LISTA)):
    if LISTA[c]['Idade'] > MEDIA:
        print(f'{LISTA[c]["Nome"]}', end=', ')
print()
