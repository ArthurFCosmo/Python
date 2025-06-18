valor = int(input('Digite o valor a ser sacado (Múltiplo de 5): R$ '))
for laco in range (1, 6, 1):
    if laco == 1:
        v = 100
    if laco == 2:
        v = 50
    if laco == 3:
        v = 20
    if laco == 4:
        v = 10
    if laco == 5:
        v = 5
    if valor >= v:
        valorv = valor // v
        valor = valor % v
        print(f'Sairão {valorv} notas de {v}')
print('Fim')
