numeroi = int(input('Digite o número inicial: '))
numero = int(input('Digite o número final: '))
numerof = numero + 1
print(f'Esses são os números pares entre {numeroi} e {numero}')
for c in range(numeroi, numerof):
    t = c % 2
    if t == 0:
        print(c)
