numero = int(input('Digite aqui o primeiro termo da progressão: '))
razao = int(input('Digite aqui a razão: '))
decimo = numero + (10 - 1) * razao
for c in range(numero, decimo + razao, razao):
    print(c, end=' -> ')
print('Fim')
