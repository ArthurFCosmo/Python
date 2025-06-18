DICIONARIOGRANDE = []
GOLS = []

while True:
    DICIONARIO= dict()
    NOME = str(input('Nome do jogador: ')).title()
    DICIONARIO['Nome'] = NOME
    NUMERODEJOGOS = int(input(f'Quantos jogos {NOME} jogou? '))
    DICIONARIO['Número de jogos'] = NUMERODEJOGOS

    for c in range(1, NUMERODEJOGOS + 1):
        GOLS.append(int(input(f'Quantos gols {NOME} fez na partida {c}: ')))

    DICIONARIO['Gols'] = GOLS[:]
    DICIONARIO['Total'] = sum(GOLS)
    GOLS.clear()

    DICIONARIOGRANDE.append(DICIONARIO.copy())

    while True:
        ESCOLHA = str(input('Quer cadastrar mais algum jogador? [S//N]')).upper()[0]
        if ESCOLHA in 'SN':
            break
        print('Apenas "S" ou "N"')
    if ESCOLHA == 'N':
        break

print(DICIONARIOGRANDE)

print('=-' * 30)
print('Jogador // Nome // Nº jogos // Gols // Total')
print('=-' * 30)
for k, v in enumerate(DICIONARIOGRANDE):
    print(f'{k:^5} // {DICIONARIOGRANDE[k]["Nome"]:^9} // {DICIONARIOGRANDE[k]["Número de jogos"]:^3} // {DICIONARIOGRANDE[k]["Gols"]} // {DICIONARIOGRANDE[k]["Total"]}')
print('=-' * 30)
print()

while True:
    while True:
        ESCOLHA = str(input('Quer mostrar os dados de algum jogador? [S//N]: ')).upper()[0]
        if ESCOLHA == 'N':
            break
        if ESCOLHA not in 'SN':
            print('Apenas "S" ou "N"')
        JOGADOR = int(input('Digite o código do jogador: '))
        if JOGADOR >= len(DICIONARIOGRANDE):
            print('Apenas código de jogadores!')
        for k, v in enumerate(DICIONARIOGRANDE[JOGADOR]['Gols']):
            print(f'No jogo {k+1} {DICIONARIOGRANDE[JOGADOR]["Nome"]} fez {v} gols')
    if ESCOLHA == 'N':
        break

print('Programa finalizado.')

DICIONARIOGRANDE = []
CONT = 0
while True:
    DICIONARIO = {}
    DICIONARIO['COD'] = CONT
    DICIONARIO['NOME'] = str(input("Nome: ")).strip().title()
    DICIONARIO['OVR'] = int(input("OVR: "))
    DICIONARIOGRANDE.append(DICIONARIO.copy())
    CONT += 1
    CONTINUA = int(input("Continuar [0 ou 1]?: "))
    if CONTINUA == 0:
        break
