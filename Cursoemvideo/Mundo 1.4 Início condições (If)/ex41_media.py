n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
mediaf = f'{media:.1f}'
if mediaf < '5':
    print(f'Sua média foi {mediaf} Infelizmente você foi reprovado.')
elif '5' >= mediaf < '7':
    print(f'Sua média foi {mediaf} Você está de recuperação.')
elif mediaf >= '7':
    print(f'Sua média foi {mediaf} Você foi aprovado.')
