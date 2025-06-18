# Pedir 7 valores
# Lista com os valores ímpares em ordem crescente
# Lista com os valores pares em ordem cresente
# Uma lista com todos os valores em duas listas internas e depois separa ela em duas listas externas

#LISTA = []
#LISTA_AUX = []
#LISTA_PAR = []
#LISTA_IMPAR = []

#for LACO_PERGUNTAS in range(0, 7):
#    LISTA_AUX.append(int(input('Digite um valor: ')))
#
 #   if LISTA_AUX[LACO_PERGUNTAS] % 2 == 0:
  #      LISTA_PAR.append(LISTA_AUX[LACO_PERGUNTAS])
#
 #   else:
  #      LISTA_IMPAR.append(LISTA_AUX[LACO_PERGUNTAS])
#
#LISTA.append(LISTA_AUX[:])
#LISTA_AUX.clear()

#LISTA_PAR.sort()
#LISTA_IMPAR.sort()

#print(f'Os numeros digitados foram: {LISTA}')
#print(f'Os números pares digitados foram: {LISTA_PAR}')
#print(f'Os números ímpares digitados foram: {LISTA_IMPAR}')

LISTA = [[],[]]
VALOR = 0

for c in range(1, 8):
    VALOR = int(input(f'Digite o {c}º valor: '))
    if VALOR % 2 == 0:
        LISTA[0].append(VALOR)
    else:
        LISTA[1].append(VALOR)

LISTA[0].sort()
LISTA[1].sort()

print(f'Os valores pares inseridos foram: {LISTA[0]}')
print(f'Os valores ímpares inseridos foram: {LISTA[1]}')
