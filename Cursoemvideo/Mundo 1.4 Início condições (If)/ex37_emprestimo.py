print('=-' * 40)
print('Bom dia, nós da Cosmos vamos iniciar o processo de aprovação do seu empréstimo!\na parcela não deve execder 30% do seu salário mensal.')
print('=-' * 40)
print('\n')
emprestimo = float(input('Qual o valor do seu empréstimo? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
anos = int(input('Em quantos anos você quer pagar? '))
meses = anos * 12
parcela = emprestimo / meses
parcelasalario = parcela * 100 / salario
if parcelasalario >= 30:
    print(f'Seu empréstimo foi negado, pois a parcela corresponde a R${parcela:.2f} ({parcelasalario:.0f}% do seu salário).')
else:
    print(f' Seu empréstimo foi aprovado! A mensalidade será de R${parcela:.2f} aplicada durante {anos} anos.')
