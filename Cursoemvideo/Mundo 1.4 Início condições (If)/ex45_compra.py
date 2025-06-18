print('=' * 20, ' LOJAS COSMO ', '=' * 20)
preco = float(input('Digite aqui o preço das compras: R$ '))
print('')
print('-=' * 20)
print('''Opções de pagamento:
[1] À vista (Dinheiro/Cheque) = 10% de desconto
[2] À vista (Cartão) = 5% de desconto
[3] Até 2x no cartão = preço normal
[4] 3x ou mais no cartão = 20% de juros''')
print('-=' * 20)
print('')
fp = int(input('Qual sua forma de pagamento? '))
print('')
if fp == 1:
    valor = preco - (preco * 0.10)
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f}')
elif fp == 2:
    valor = preco - (preco * 0.05)
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f}')
elif fp == 3:
    valor = preco
    parcela = preco / 2
    print(f'Sua compra será parcelada em 2 vezes de R${parcela:.2f} sem juros.')
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f}')
elif fp == 4:
    valor = preco + (preco * 0.2)
    parcelas = int(input('Em quantas vezes voê quer parcelar? '))
    print('')
    parcela = valor / parcelas
    print(f'Sua será parcelada em {parcelas} vezes de R${parcela:.2f} com 20% de juros.')
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f}')
else:
    print('Forma de pagamento inválida! Digite 1, 2, 3 ou 4')
