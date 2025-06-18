contador = 0
acumulador = 0
for c in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        contador += 1
        acumulador += numero
print(f'A quantidade de números pares informados é {contador} e sua soma é {acumulador}')
