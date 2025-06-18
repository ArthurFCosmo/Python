# Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios (1 número)
# guarde os resultados em um dicionário
# coloque esse dicionário em ordem com o vencedor tendo o maior numero

from random import randint
from operator import itemgetter

DICT = {'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6)}

print()
for k, v in DICT.items():
    print(f'{k} tirou {v} no dado')

RANKING = sorted(DICT.items(), key=itemgetter(1), reverse=True)

print('==' * 30)

for key, value in enumerate(RANKING):
    print(f'O jogador {value[0]} tirou {value[1]} e ficou em {key+1}º')
