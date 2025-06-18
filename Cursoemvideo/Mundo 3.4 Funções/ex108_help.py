def ajuda(F):
    print(help(F))
 
while True:
    AJUDA = input('Digite aqui a função ou biblioteca: ').lower()
    if AJUDA == 'fim':
        break
    ajuda(AJUDA)
print('Programa finalizado.')
