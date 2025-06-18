k = float(input('Quantos km o carro rodou?'))
d = int(input('Por quantos dias o carro esteve alugado?'))
p = (k * 0.15) + (d * 60)
print(f'O preço a pagar pelo aluguel do carro é de R$ {p:.2f}')
