def leiaint(texto):
    while True:
        num = input(f'{texto} ')
        if not num.isnumeric():
            print('\033[0;31mDigite apenas valores numéricos!\033[m')
        else:
            break
    return f'{num}'


n = leiaint('Digite um número:')
print(f'Você digitou o número {n}')
