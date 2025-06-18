import random
import time
numero = random.randint(0, 5)
print('-=' * 16)
print('Vou pensar em um número de 0 a 5!')
print('-=' * 16)
time.sleep(2)
print('Processando...')
time.sleep(3)
jogador = int(input('Em qual número você acha que eu pensei? '))
if numero == jogador:
    print(f'Caramba! Você acertou, eu realmente tinha pensado no {numero}...')
else:
    print(f'Haha você errou! eu tinha pensado no {numero} e não no {jogador}')
