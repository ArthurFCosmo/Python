soma = quantidade = 0
while True:
    numero = int(input('Digite um número (digite 999 para parar): '))
    if numero == 999:
        break
    soma += numero
    quantidade += 1
print('')
print(f'Você digitou {quantidade} números, a soma entre eles vale {soma}')
print('Finalizado!')
