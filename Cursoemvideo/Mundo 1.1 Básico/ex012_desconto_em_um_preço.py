valor = float(input('Qual o valor do produto? '))
d = int(input('Qual a % do desconto? '))
v = valor - (d / 100 * valor)
print(f'O valor do produto é de R$ {v:.2f}')
