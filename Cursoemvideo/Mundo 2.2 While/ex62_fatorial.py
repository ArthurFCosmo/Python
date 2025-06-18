numero = int(input('Digite um valor para saber seu fatorial: '))
soma = 0
for laco in range(numero - 1, -1, -1):
    print(f'{numero} x {laco} = {numero*laco}', end=' // ')
    soma += numero * laco
print('')
print(f'{numero}! = {soma}')
