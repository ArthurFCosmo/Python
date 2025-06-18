# Crie uma matriz 3x3 na tela (tipo o teclado num)
# Coloque um input pra preencher os 9 valores
# Salvar os dados em uma estrutura única

LISTA = []
DADOS = []

for perguntas in range(0 ,9):
    DADOS.append(int(input('Digite um valor: ')))
    LISTA.append(DADOS[:])
    DADOS.clear()

print(f'''{LISTA[0]}   {LISTA[1]}   {LISTA[2]}
{LISTA[3]}   {LISTA[4]}   {LISTA[5]}
{LISTA[6]}   {LISTA[7]}   {LISTA[8]}''')
