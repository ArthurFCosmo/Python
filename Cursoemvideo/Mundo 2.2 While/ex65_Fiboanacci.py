termos = int(input('Quantos termos da sequência de fibonacci você quer ver? '))
t1 = 0
t2 = 1
contador = termos
print(f'{t1} --> {t2}', end='')
while contador != 0:
    t3 = t1 + t2
    print(f' --> {t3}', end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    contador -= 1
print(' --> FIM')