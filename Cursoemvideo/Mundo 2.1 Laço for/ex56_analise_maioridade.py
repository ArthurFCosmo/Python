from datetime import date
maiores = 0
menores = 0
anoatual = date.today().year
for pergunta in range(1, 8):
    nascimento = int(input(f'Em qual ano a {pergunta} pessoa nasceu? '))
    if nascimento > anoatual - 18:
        menores += 1
    else:
        maiores += 1
print(f'Na pesquisa tiveram {maiores} maiores de idade e {menores} menores de idade.')
