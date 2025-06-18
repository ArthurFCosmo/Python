# Pedir o nome do aluno e mais duas notas para vários alunos em uma lista única
# Lançar um boletim com a média de cada um
# O usuário pode pedir a nota de um aluno em específico

LISTA = []
AUX = []

QUANTIDADE = int(input('Quantos alunos você quer cadastrar? '))

for c in range(1, QUANTIDADE + 1):
    nome = input(f'Digite o nome do aluno {c}: ')
    nota1 = float(input(f'Digite aqui a 1º nota do aluno {c}: '))
    nota2 = float(input(f'Digite aqui a 2º nota do aluno {c}: '))

    AUX.append(nome)
    AUX.append(nota1)
    AUX.append(nota2)

    print('==' * 30)

    LISTA.append(AUX[:])
    AUX.clear()

print('==' * 30)
print(f'{"Aluno":<10}{"Nota1":^7}{"Nota2":^7}{"Média":^7}')
print('==' * 30)

for a in range(0, QUANTIDADE):
    media = (LISTA[a][1] + LISTA[a][2]) / 2
    print(f'{LISTA[a][0]:<10}{LISTA[a][1]:^7.2f}{LISTA[a][2]:^7.2f}{media:^7.2f}')
    
print('==' * 30)
