soma = 0
somamaisvelho = ''
contadornova = 0
nomemaisvelho = ''
for laco1 in range(1, 6):
    print(f'=========== {laco1}º pessoa =========== ')
    nome = str(input('Digite seu nome: ')).capitalize()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M] ou [F]: ')).upper()
    soma += idade
    if laco1 == 1:
        somamaisvelho = idade
    if idade > somamaisvelho:
        somamaisvelho = idade
    if somamaisvelho == idade:
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        contadornova += 1
media = soma / 5
print('=' * 35)
print(f'A média das idades dos candidatos foi {media} anos.')
print(f'O candidato mais velho é {nomemaisvelho} e ele tem {somamaisvelho} anos.')
print(f'Foram cadastradas {contadornova} candidatas com menos de 20 anos.')
