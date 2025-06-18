r1 = float(input('Digite o comprimento de um segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 = float(input('Digite o comprimento do terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não formam um triângulo.')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
    print('As retas formam um triângulo isóceles.')
elif r1 == r2 == r3:
    print('As retas formam um triângulo equilátero.')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 != r3 != r1:
    print('As retas formam um triângulo escaleno.')
