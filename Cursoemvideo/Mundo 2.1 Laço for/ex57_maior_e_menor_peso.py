pesado = 0
leve = 0
for laco in range(1, 6):
    peso = int(input(f'Peso da {laco}º pessoa: '))
    if laco == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        elif peso < leve:
            leve = peso
print(f'O menor peso foi {leve}')
print(f'O maior peso foi {pesado}')
