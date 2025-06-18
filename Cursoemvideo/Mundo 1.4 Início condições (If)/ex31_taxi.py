viagem = float(input('Digite a distância da viagem em km: '))
if viagem <= 200:
    taxa = viagem * 0.5
    print(f'Sua viagem custará R${taxa:.2f}')
else:
    taxa2 = viagem * 0.45
    print(f'Sua viagem custará R${taxa2:.2f}')
