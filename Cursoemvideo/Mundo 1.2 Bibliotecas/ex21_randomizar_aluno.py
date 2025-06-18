import random
a1 = input('Digite o nome de um aluno')
a2 = input('Digite o nome de outro aluno')
a3 = input('Digite o nome de mais um aluno')
a4 = input('Digite o nome de mais outro aluno')
lista = [a1, a2, a3, a4]
print(f'O aulo sorteado pelo sistema de aleatóriedade foi {random.choice(lista)}')
