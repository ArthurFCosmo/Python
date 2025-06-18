lista = []
for laco in range(1, 6):
    valor = int(input(f'Digite um valor para a posição {laco}: '))
    lista.append(valor)
print(lista)
print(f'O maior valor na lista foi {max(lista)}')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'O valor foi encontrado na posição {i+1}')
print(f'O menor valor na lista foi {min(lista)}')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'O valor foi encontrado na posição {i+1}')
