import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno do seu ângulo é {seno:.3f}\nO coseno é {coseno:.3f}\nA tangente é {tangente:.3f}')
