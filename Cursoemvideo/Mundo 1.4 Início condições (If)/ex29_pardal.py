velocidade = int(input('Digite a velocidade do carro: '))
multa = float((velocidade - 80) * 7)
if velocidade >= 80:
    print(f'Você está {velocidade} Km/h, a velocidade máxima permitida é de 80 Km/h!')
    print(f'Você será multado em R${multa:.2f}')
else:
    print('Você está dentro da velocidade permitida')
print('Fim')
