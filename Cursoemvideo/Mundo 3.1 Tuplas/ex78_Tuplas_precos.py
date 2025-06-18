listagem = ('Acucar', 3.50, 'Pão', 2, 'Manteiga', 8, 'margarina', 3, 'Feijão', 10,
            'Arroz', 4, 'Aveia', 3.50, 'Bolacha', 5.50)
print('=' * 30)
print(f'{"Preços":^30}')
print('=' * 30)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<21}', end='')
    print(f'R${listagem[c+1]:>5.2f}')
print('=' * 30)
