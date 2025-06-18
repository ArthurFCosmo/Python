v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite o penultimo valor: '))
v4 = int(input('Digite digite o ultimo valor: '))
tupla = (v1, v2, v3, v4)
print(f'Na tupla o número nove aparece {tupla.count(9)} vezes.')
if tupla.count(3) != 0:
    print(f'O valor 3 aparece na {tupla.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não aparece na tupla.')
tuplapares = ''
for c in tupla:
    if c % 2 == 0:
        tuplapares += f' {c}'
print(f'Os valores pares na tupla foram {tuplapares.strip()}')
