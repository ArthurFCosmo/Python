from random import randint
print('=' * 12)
print('PAR OU ÍMPAR')
print('=' * 12)
print('')
vitorias = 0
while True:
    while True:
        valor = int(input('Digte o valor que você vai jogar (Abaixo de 10): '))
        if valor > 10:
            print('Por favor, insira um valor abaixo de 10!')
        else:
            break
    while True:
        escolha = str(input('Vai apostar impar ou par [P] ou [I]? ')).strip().upper()[0]
        if escolha not in 'PI':
            print('Por favor, digite apenas [P] para par ou [I] para ímpar!')
        else:
            break
    jogadapc = randint(0, 10)
    soma = jogadapc + valor
    teste = soma % 2
    if teste == 0 and escolha == 'P':
        vitorias += 1
        print('=' * 20)
        print(f'Eu joguei {jogadapc} e você {escolha}, a soma deu {soma}, que é par. Você venceu! ')
        print('=' * 20)
    elif teste != 0 and escolha == 'I':
        vitorias += 1
        print('=' * 20)
        print(f'Eu joguei {jogadapc} e você {escolha}, a soma deu {soma}, que é ímpar. Você venceu!')
        print('=' * 20)
    elif teste != 0 and escolha == 'P':
        print('=' * 20)
        print(f'Eu joguei {jogadapc} e você {escolha}, a soma deu {soma}, que é ímpar. Você perdeu!')
        print('=' * 20)
        break
    else:
        print('=' * 20)
        print(f'Eu joguei {jogadapc} e você {escolha}, a soma deu {soma}, que é par. Você perdeu! ')
        break
print('')
print(f'Você conseguiu um total de {vitorias} vitórias!')
