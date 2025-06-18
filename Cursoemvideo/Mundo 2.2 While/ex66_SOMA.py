print('Digite 999 para parar.')
quantidade = soma = 0
numero = int(input('Digite um número inteiro: '))
while numero != 999:
    quantidade += 1
    soma += numero
    numero = int(input('Digite um número inteiro: '))
print()
print(f'Você digitou {quantidade} números.')
print(f'A soma dos números que você digitou vale {soma}')
