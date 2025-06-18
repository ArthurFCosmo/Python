import random
import time
numero = random.randint(0, 10)
print('-=' * 16)
print('Vou pensar em um número de 0 a 10!')
print('-=' * 16)
time.sleep(2)
print('Processando...')
print()
time.sleep(3)
jogador = 100
contador = 0
while jogador != numero:
    jogador = int(input('Em qual número você acha que eu pensei? '))
    contador += 1
    if jogador != numero:
        if jogador > numero:
            print()
            print('=' * 40)
            print('Voce errou pra MAIS tente novamente!')
            print('=' * 40)
            print()
        else:
            print()
            print('=' * 40)
            print('Voce errou pra MENOS tente novamente!')
            print('=' * 40)
            print()
print()
print(f'Você acertou! Eu tinha pensado no {numero}...')
print(f'Você levou {contador} tentativas para acertar.')
