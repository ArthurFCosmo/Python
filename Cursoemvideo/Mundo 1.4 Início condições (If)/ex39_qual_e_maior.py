v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
if v1 > v2:
    print(f'{v1} é maior que {v2}!')
elif v2 > v1:
    print(f'{v2} é maior que {v1}')
elif v1 == v2:
    print('Os dois valores são iguais!')
