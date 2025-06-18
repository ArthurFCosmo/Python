### faça um programa que tenha uma função chamada área() , que receba largura e comprimento e retorne a área

def área(L, C):
    AREA = L * C
    print(f'A área do terreno é {AREA} m²')


COMPRIMENTO = float(input('Digite aqui o comprimento do terreno em metros: '))
LARGURA = float(input('Digite aqui a largura do terreno: '))

área(COMPRIMENTO, LARGURA)
