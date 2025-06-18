nome = input('Nome do aluno: ')
at1 = float(input('Qual a nota de sua avaliação parcial? '))
at2 = float(input('Qual a nota de sua avaliação global? '))
media = (at1 + at2) / 2
print(f'A média semestral de {nome} foi de {media:.1f}')
