lista = []
for laco in range(0, 5):
    valor = int(input('Digite um valor para adicionar à lista: '))
    if laco == 0 or laco == -1:
        lista.append(valor)
        print('Adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(f'Os valores em ordem colocados na lista foram {lista}')
