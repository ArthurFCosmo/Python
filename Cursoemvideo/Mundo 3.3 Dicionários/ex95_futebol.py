# Crie um progarama que gerencie o aroveitamento de um jogador de futebol
# O programa vai ler o nome do jogador e quantas partidas ele jogou
# Depois vai ler a quantidade de gols feitos em cada partida
# No final, tudo isso será guardado em um dicionário
# incluindo o total de gols feitos durante o campeonato

GOLS = []
RELATORIO = {}

NOME = str(input('Nome: ')).strip().title()
PARTIDAS = int(input('Quantas partidas o jogador jogou? '))

TOTAL = 0
for c in range(1, PARTIDAS + 1):
    GOLS.append(int(input(f'Quantos gols {NOME} fez na partida {c}? ')))

RELATORIO['Nome'] = NOME
RELATORIO['Gols'] = GOLS[:]
RELATORIO['Total de gols'] = sum(GOLS)

print('=-=-=' * 15)
print(RELATORIO)
print('=-=-=' * 15)

for key, value in RELATORIO.items():
    print(f'{key}: {value}')

print('=-=-=' * 15)
print(f'O jogador {NOME} jogou {PARTIDAS} partidas.')

for c in range(1, PARTIDAS + 1):
    print(f'Na partida {c}, {NOME}, fez {RELATORIO["Gols"][c-1]} gols.')
print(f'Foi um total de {RELATORIO["Total de gols"]}')
print('=-=-=' * 15)
