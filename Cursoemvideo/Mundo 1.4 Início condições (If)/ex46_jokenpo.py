import random
from time import sleep
print('\033[1;32m=' * 10, ' Pedra Papel e Tesoura ', '=' * 10)
print('\033[m')
print('\033[36mVou pensar na minha jogada,')
sleep(3)
print('depois você escolhe a sua !')
sleep(3)
print('eu vou contar até 3, e no 3 a gente vê quem ganhou ok?')
pedra = 1
papel = 2
tesoura = 3
lista = [pedra, papel, tesoura]
jogadapc = random.choice(lista)
sleep(5)
print('...')
sleep(4)
print('Pronto, ja escolhi qual eu vou jogar!')
print('')
print('''\033[32m[1]Pedra
[2]Papel
[3]Tesoura''')
print('\033[36m')
jogada = int(input('E você? qual a sua jogada? '))
sleep(1)
print('Certo, vou contar até 3 e a gente vê o resultado! ')
sleep(2)
print('1...')
sleep(1)
print('2...')
sleep(1)
print('3!')
print('')
print('\033[1;32m='*30)
if jogadapc == 1:
    print(f'Minha jogada foi PEDRA!')
    if jogada == 1:
        print('Sua jogada foi PEDRA também!')
        print('=' * 30)
        print('Empatamos!')
    if jogada == 2:
        print('Sua jogada foi Papel!')
        print('=' * 30)
        print('Você venceu...')
    if jogada == 3:
        print('Sua jogada foi TESOURA!')
        print('=' * 30)
        print('Eu venci!')
elif jogadapc == 2:
    print(f'Minha jogada foi PAPEL!')
    if jogada == 1:
        print('Sua jogada foi PEDRA!')
        print('=' * 30)
        print('Eu venci!')
    if jogada == 2:
        print('Sua jogada foi PAPEL também!')
        print('=' * 30)
        print('Empatamos!')
    if jogada == 3:
        print('Sua jogada foi TESOURA!')
        print('=' * 30)
        print('Você venceu...')
elif jogadapc == 3:
    print(f'Minha jogada foi TESOURA!')
    if jogada == 1:
        print('Sua jogada foi PEDRA!')
        print('=' * 30)
        print('Você venceu...')
    if jogada == 2:
        print('Sua jogada foi PAPEL!')
        print('=' * 30)
        print('Eu venci!')
    if jogada == 3:
        print('Sua jogada foi TESOURA')
        print('=' * 30)
        print('Empatamos!')
