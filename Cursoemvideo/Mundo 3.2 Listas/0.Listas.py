# variavel

lista = [1, 3, 2, 0, 7]
print(lista)
lista[1] = 8
print(lista)
lista.append(4)
print(lista)
lista.insert(0, 0)
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(f'Essa lista tem {len(lista)} elementos')
lista.pop()
print(lista)
lista.pop(2)
print(lista)
lista.remove(8)
print(lista)

# for

valores = list()
valores.append(5)
valores.append(3)
valores.append(6)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

# cópias

a = [2, 4, 7, 8]
b = a[:]
b[2] = 1
print(a)
print(b)
