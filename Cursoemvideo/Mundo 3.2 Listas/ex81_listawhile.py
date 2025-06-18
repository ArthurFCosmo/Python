lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('O valor já foi indicado anteriormente e não será registrado.')
        continuar = str(input('Quer adicionar mais algum valor [S/N]? ')).strip().upper()[0]
        if continuar == 'N':
            break
    else:
        lista.append(valor)
        print('O valor foi adicionado!')
        continuar = str(input('Quer adicionar mais algum valor [S/N]? ')).strip().upper()[0]
        if continuar == 'N':
            break
lista.sort()
print(lista)
