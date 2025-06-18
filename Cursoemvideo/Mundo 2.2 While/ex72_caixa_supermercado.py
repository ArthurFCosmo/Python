print('=' * 10)
print('LOJA COSMO')
print('=' * 10)
print('')
print('Registro de compras')
print('')
print('=' * 70)
nome = str(input('Digite seu nome completo: ')).strip().capitalize()
email = str(input('Digite aqui seu email: ')).strip()
print('=' * 70)
soma = maisdemil = produtos = 0
maisbarato = ''
while True:
    print('')
    while True:
        produto = str(input('Digite aqui o produto: ')).strip()
        if produto.isnumeric() is False:
            break
    valor = float(input('Digite aqui o valor do produto: R$ '))
    quantidade = int(input('Digite aqui a quantidade: '))
    valortotal = valor * quantidade
    soma += valortotal
    produtos += quantidade
    if valor > 1000:
        maisdemil += 1
    if produtos == 1:
        maisbarato = produto
    if produto < maisbarato:
        maisbarato = produto
    print('=' * 70)
    continua = str(input('Quer registrar mais alguma compra [S] ou [N]? ')).strip().upper()[0]
    if continua == 'N':
        break
print('=' * 70)
print('Registro de compras finalizado !')
print(f'Foram registrados {produtos} produtos, somando um valor de R$ {soma:.2f}')
print(f'Foram registrados {maisdemil} produtos com valor acima de R$ 1000,00')
print(f'O produto mais barato registrado foi "{maisbarato}"')
print('=' * 70)
print(f'Pagador: {nome}')
print(f'Entraremos em contato através do seu e-mail {email} para iformar sobre a entrega de suas mercadorias!')
