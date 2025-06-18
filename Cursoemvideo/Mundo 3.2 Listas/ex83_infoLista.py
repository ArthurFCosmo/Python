lista = []
while True:
    valor = int(input('Digite um valor para adicionar a lista: '))
    lista.append(valor)
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar != 'S' and continuar != 'N':
        print('Por favor digite um valor válido!')
    if continuar == 'N':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor foi 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')
