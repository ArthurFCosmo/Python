lista = []
listapar = []
listaimpar = []
while True:
    valor = int(input('Digite um valor para adicionar a lista: '))
    lista.append(valor)
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar != 'S' and continuar != 'N':
        print('Por favor digite um valor válido!')
    if continuar == 'N':
        break
print(lista)
print(listapar)
print(listaimpar)
