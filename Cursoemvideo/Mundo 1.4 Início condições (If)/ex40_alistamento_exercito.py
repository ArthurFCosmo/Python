idade = int(input('Qual a sua idade? '))
alistamento = 18
falta = 18 - idade
passaram = idade - 18
if idade == alistamento:
    print('Já está na hora de se alistar no exército!')
elif idade < alistamento:
    print(f'Faltam {falta} anos para você se alistar no exército')
elif idade > alistamento:
    print(f'Já passou da hora de você se alistar no exército!\nVocê deveira ter se alistado {passaram} anos atrás!')
    print('Aliste-se o quanto antes!')
