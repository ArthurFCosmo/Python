soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(f'A soma de todos os {contador} valores múltiplos de 3 entre 0 e 500 são {soma}')
