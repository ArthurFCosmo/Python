# Crie um programa que leia nome, ano de nascimento e carteira da trabalho
# e cadastre-os (com idade) em um dicionário
# Se por acaso a carteira de trabalho for diferente de ZERO
# O dicionário receberá também o ano de contratação e o salário
# Calcule e acrescente com quantos anos a pessoa vai se aposentar

from datetime import datetime

DICT = {}

DICT['Nome'] = str(input('Digite o nome da pessoa: ')).strip().title()
NASCIMENTO = int(input('Digite o ano de nascimento da pessoa: '))
DICT['Idade'] = datetime.now().year - NASCIMENTO
DICT['CT'] = int(input('Digite aqui o número da carteira de trabalho da pessoa (Digite 0 se não tiver): '))

if DICT['CT'] != 0:
    DICT['Contratação'] = int(input('Digite o ano de contratação da pessoa: '))
    DICT['Salário'] = float(input('Digite o salário da pessoa: '))
    DICT['Aposentadoria'] = DICT['Idade'] + ((DICT['Contratação'] + 35) - datetime.now().year)

print()
print('=' * 30)
print()

for key, value in DICT.items():
    print(f'{key}: {value}')
