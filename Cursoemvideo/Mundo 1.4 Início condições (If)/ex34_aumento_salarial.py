#um programa que pergunte o salário de um funcionário e aumente 10% para valores acima de 1250, 15% para valores abaixo#
salario = float(input('Digite aqui seu salário para ser reajustado: '))
maior = salario * 1.10
menor = salario * 1.15
if salario >= 1250:
    print(f'Seu novo salário será de R${maior:.2f} após um aumento de 10%')
else:
    print(f'Seu novo salário será de R${menor:.2f} após um aumento de 15%')
