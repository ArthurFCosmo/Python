ano = int(input('Digite o ano que você quer saber: '))
teste = ano % 4
if teste == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')
