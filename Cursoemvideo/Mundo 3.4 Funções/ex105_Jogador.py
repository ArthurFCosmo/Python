def ficha(J='Desconhecido', G=0):
    print(f'O jogador {J} fez {G} gol(s).')


JOGADOR = str(input('Nome do jogador: ')).title().strip()
GOLS = str(input('Número de gols: '))
if GOLS.isnumeric():
    GOLS = int(GOLS)
else:
    GOLS = 0
if JOGADOR == '':
    ficha(G=GOLS)
else:
    ficha(JOGADOR, GOLS)
