altura = float(input('Digite aqui sua altura em metros com centímetros: '))
peso = float(input('Digite aqui seu peso: '))
imc = peso / (altura ** 2)
print(f'Seu imc é de: {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 >= imc < 25.0:
    print('Você está no peso ideal!')
elif 25.0 >= imc < 30.0:
    print('Você está com sobrepeso!')
elif 30.0 >= imc <= 40.0:
    print('Você está com obesidade!')
elif imc > 40.0:
    print('Você está com obesidade mórbida!')
