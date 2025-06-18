numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    digito = int(input('Digite um número entre 0 e 20: '))
    if digito > 20 or digito < 0:
        print('Digite um número entre 0 e 20!')
    else:
        break
print(f'Você digitou o número {numeros[digito-1]}.')
