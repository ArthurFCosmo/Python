def maior(* num):
    print('Analisando os valores passados...')
    for valor in num:
        print(f' {valor} ', end='')
    print()
    print(f'O maior valor foi: {max(num)}')

# programa principal
maior(0, 1 ,23 ,435, 653 ,231 ,123)
maior(1, 3, 5, 3, 6, 7, 3)
maior(1, 2)
maior(6)
