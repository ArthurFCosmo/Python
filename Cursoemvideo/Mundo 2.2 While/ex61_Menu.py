from time import sleep
limpa = '\033[m'
branco = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
print('=' * 30)
print('Calculadora para dois valores')
print('=' * 30)
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('')
    print('...')
    sleep(2)
    print('')
    opcao = int(input(f'''Escolha a operação para relacionar os valores:
    
{verde}[1] Soma
[2] Mutiplicação
[3] Qual o maior
[4] Quero digitar valores diferentes
[5] Sair{limpa}

Sua opção: '''))
    if opcao == 1:
        print('')
        print(f'{verde}A soma dos valores vale {numero1+numero2}{limpa}')
    elif opcao == 2:
        print('')
        print(f'{verde}A mutiplicação entre os valores vale {numero1 * numero2}{limpa}')
    elif opcao == 3:
        print('')
        if numero1 > numero2:
            print(f'{verde}{numero1} é maior que {numero2}{limpa}')
        elif numero2 > numero1:
            print(f'{verde}{numero2} é maior que {numero1}{limpa}')
    elif opcao == 4:
        print('')
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número:'))
    else:
        print('')
        print(f'{vermelho}Digite uma opção válida!{limpa}')
print('')
print(f'{verde}Espero ter ajudado!{limpa}')
