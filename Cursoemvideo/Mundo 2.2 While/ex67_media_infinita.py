resposta = 'S'
soma = quantidade = maior = menor = numero = 0
while resposta == 'S':
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar [S] ou [N]? ')).upper().strip()[0]
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    print()
media = soma / quantidade
print(f'Você digitou {quantidade} números e a soma vale {soma}')
print(f'A média entre esses números vale {media}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
