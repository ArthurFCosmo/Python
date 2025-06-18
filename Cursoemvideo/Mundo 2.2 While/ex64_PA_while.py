termo1 = int(input('Digite aqui o primeiro termo de sua PA: '))
razao = int(input('Digite aqui a razão da PA: '))
contador = 1
while contador != 11:
    print(f'{contador} termo = {termo1}')
    termo1 += razao
    contador += 1
escolha = ''
while escolha != 'N':
    print('')
    escolha = str(input('Você quer mostrar mais algum termo [S] ou [N]? ')).upper()
    if escolha == 'S':
        termos = int(input('Quantos termos a mais você quer ver? '))
        contatermos = 0
        while contatermos != termos:
            print(f'{contador} termo = {termo1}')
            contador += 1
            termo1 += razao
            termos -= 1
print('')
print('Espero ter ajudado!')
