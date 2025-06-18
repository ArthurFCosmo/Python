lista = list()
listaaux = list()
for laco in range(0, 4):
    listaaux.append(str(input('Digite aqui o nome do candidato: ')))
    listaaux.append(int(input('Digite aqui a idade do candidato: ')))
    lista.append(listaaux[:])
    listaaux.clear()

print(lista)
