palavra = str(input('Digite uma frase e direi se ela é um palíndromo: ')).strip().replace(' ', '').upper()
len = len(palavra)
inverso = ''
for laco in range(len-1, -1, -1):
    print(palavra[laco], end='')
    inverso += palavra[laco]
if inverso == palavra:
    print('\nPalíndromo!')
else:
    print('\nNão é um palíndromo')
