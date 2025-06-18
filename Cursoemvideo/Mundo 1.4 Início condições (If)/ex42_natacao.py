idade = int(input('Digite sua idade para definirmos sua categoria: '))
if idade <= 9:
    print('Você pertence à categoria mirim!')
elif idade > 9 <= 14:
    print('Você pertence à categoria infantil!')
elif idade > 14 <= 19:
    print('Você pertence à categoria júnior!')
elif idade > 19 <= 25:
    print('Você pertence à categoria sênior!')
elif idade > 25:
    print('Você pertence à categoria sênior!')
