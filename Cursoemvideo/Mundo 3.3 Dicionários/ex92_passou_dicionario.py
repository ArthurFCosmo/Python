# Faça um programa que leia o nome e média de um aluno,
# guardando também a situação (passou ou nao) em um dicionário
# depois printe tudo
DICT = {}

DICT['NOME'] = str(input('Digite o nome do aluno: ')).strip().title()
DICT['MEDIA'] = float(input('Digite a média do aluno (0 a 10): '))

if DICT['MEDIA'] < 7:
    DICT['COND'] = 'REPROVADO'
else:
    DICT['COND'] = 'APROVADO'

print('=====' * 10)
for key, value in DICT.items():
    print(f'{key}: {value}')
print('=====' * 10)
