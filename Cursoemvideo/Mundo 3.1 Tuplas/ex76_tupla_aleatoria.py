from random import randint
maior = menor = 0
lista = (randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000))
print('=' * 30)
print(f'{" Lista ":-^30}')
print('=' * 30)
for c in range(0, len(lista)):
    print(f'{lista[c]:^30}')
print('=' * 30)
print(f'O maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')
