import random
a1 = str(input('Digite o nome de um aluno '))
a2 = str(input('Digite o nome de outro aluno '))
a3 = str(input('Digite o nome de mais um aluno '))
a4 = str(input('Digite o nome do ultimo aluno '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'A ordem de apresentação dos trabalhos será {lista}')
