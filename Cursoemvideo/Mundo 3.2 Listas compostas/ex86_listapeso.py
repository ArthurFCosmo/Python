# LISTA // QUANTAS PESSOAS FORAM CADASTRADAS
# LISTA COM PESSOAS MAIS PESADAS (SE TIVER MAIS DE UMA)
# LISTA COM PESSOAS MAIS LEVES (SE TIVER MAIS DE UMA)

lista = []  
listaaux = []
while True:
    listaaux.append(str(input('Digite o primeiro nome da pessoa: ')).strip().capitalize())
    listaaux.append(int(input('Digite o peso da pessoa: ')))
    lista.append(listaaux[:])
    listaaux.clear()

    finalizar_input = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if finalizar_input == 'N':
        break

listapeso = []
for item in lista:
    listapeso.append(item[1])

pesado = listapeso.index(max(listapeso))
leve = listapeso.index(min(listapeso))

print(f'Lista -- {lista}')
print(f'Listapeso -- {listapeso}')


print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A pessoa mais pesada foi: {lista[pesado][0]} com {lista[pesado][1]} Kg.')
print(f'A pessoa mais leve foi: {lista[leve][0]} com {lista[leve][1]} Kg.')
