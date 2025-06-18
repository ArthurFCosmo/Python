import math
oposto = float(input('Digite o comprimento do cateto oposto do triângulo em metros:'))
adjacente = float(input('Digite o comprimento do cateto adjacente do triângulo em metros'))
hip = math.sqrt(oposto ** 2 + adjacente ** 2)
print(f'O comprimento da hipotenusa do seu triângulo, em metros, é de : {hip:.2f}')
