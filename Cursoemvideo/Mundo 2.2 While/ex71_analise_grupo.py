contadormaioridade = 0
contadorhomem = 0
mulheresmenos18 = 0
print('=' * 10)
print('Cadastros')
print('=' * 10)
while True:
    while True:
        print()
        print('=' * 40)
        idade = input('Qual a idade? ')
        if idade > '18':
            contadormaioridade += 1
        teste = idade.isalpha()
        if teste is True:
            print('Digite apenas valores numéricos!')
        break
    while True:
        sexo = str(input('Qual o sexo dessa pessoa [M] ou [F]? ')).strip().upper()[0]
        if sexo == 'M':
            contadorhomem += 1
        if sexo != 'M' and sexo != 'F':
            print('Por favor, digite [M] para masculino ou [F] para feminino!')
        if sexo == 'F' and idade < '18':
            mulheresmenos18 += 1
        print('=' * 40)
        print()
        break
    continuar = str(input('Você quer cadastrar mais um participante [S] ou [N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=' * 80)
print('Fim dos cadastros.')
print(f'Você cadastrou {contadormaioridade} pessoas maiores de 18 anos.')
print(f'Você cadastrou {contadorhomem} homens.')
print(f'Você cadastrou {mulheresmenos18} mulheres com menos de 18 anos.')
