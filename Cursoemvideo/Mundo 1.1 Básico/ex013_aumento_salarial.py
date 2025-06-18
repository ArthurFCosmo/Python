valor = int(input('Qual é o salário do funcionário? '))
aumento = int(input('Qual a % de aumento que ele deve ganhar? '))
s = aumento / 100 * valor + valor
print(f'Após um aumento de {aumento}%, o funcionário passará a ganhar R$ {s:.2f}')
