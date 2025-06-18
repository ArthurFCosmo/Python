valor = int(input('Digite o valor que você quer sacar: R$ '))
if valor >= 50:
    valor50 = valor // 50
    valor = valor % 50
    print(f'Sairão {valor50} notas de 50')
    print(f'Restará {valor}')
if valor >= 20:
    valor20 = valor // 20
    valor = valor % 20
    print(f'Sairão {valor20} notas de 20')
    print(f'Restará {valor}')
if valor >= 10:
    valor10 = valor // 10
    valor = valor % 10
    print(f'Sairão {valor10} notas de 10')
    print(f'Restará {valor}')
if valor >= 5:
    valor5 = valor // 10
    valor = valor % 10
    print(f'Sairão {valor5} notas de 5')
    print(f'Restará {valor}')
