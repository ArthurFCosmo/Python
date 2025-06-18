valor = float(input('Quantos Reais você tem na carteira? R$ '))
r = valor // 5.27
m = valor * 5.27
print(f'Você tem o equivalente a {r:.2f} Dólares.')
print(f'Se você tivesse esse mesmo valor em dólares, equivaleria {m:.2f} Reais em sua carteira')
