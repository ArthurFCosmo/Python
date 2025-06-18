numero = int(input('Digite um número e lhe retornarei seu fatorial: '))
soma = 0
c = numero
while c != 0:
    c -= 1
    soma += numero * c
    print(f'{numero} x {c} = {numero*c}')
print(f'{numero}! = {soma}')
