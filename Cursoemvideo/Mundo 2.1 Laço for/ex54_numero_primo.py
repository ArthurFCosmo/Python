numero = int(input('Digite um número e direi se ele é primo: '))
acumulador = 0
for c in range(3, 10):
    if numero % c != 0:
        print(f'\033[33m{c}\033[m', end=' ')
    elif numero % c == 0:
        print(f'\033[31m{c}\033[m', end=' ')
        acumulador += 1
if numero == 5:
    print('Seu número é primo')
elif numero == 7:
    print('Seu número é primo')
elif acumulador == 0:
    print('Seu número é primo')
else:
    print('Seu número não é primo')
