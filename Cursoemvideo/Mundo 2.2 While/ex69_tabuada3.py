while True:
    print('')
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    contagem = 10
    while contagem != 0:
        print(f'{numero} x {contagem} = {numero*contagem}')
        contagem -= 1
print('Finalizado!')
