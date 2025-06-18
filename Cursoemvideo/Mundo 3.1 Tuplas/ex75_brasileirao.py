tabela = ('Atlético MG', 'Palmeiras', 'Fortaleza', 'Flamengo',
          'Bragantino', 'Corintinhans', 'Internacional', 'Fluminense',
          'Atletico PR', 'Cuiabá', 'Ceará', 'Atlético GO', 'São Paulo',
          'Juventude', 'América MG', 'Santos', 'Bahia', 'Grêmio', 'Sport',
          'Chapecoense')
print('Tabela do Brasileirão:')
print(tabela)
print('=' * 265)
print('Os primeiros 5 colocados são:')
print(tabela[0:6])
print('=' * 265)
print('Os 4 últimos colocados são:')
print(tabela[-4:])
print('=' * 265)
print('Aqui está a tabela em ordem alfabética:')
print('=' * 265)
print(sorted(tabela))
print(f'O chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')
print('=' * 265)
