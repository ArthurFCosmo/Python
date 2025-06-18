# Crie uma matriz 3x3 na tela (tipo o teclado num)
# Coloque um input pra preencher os 9 valores
# Salvar os dados em uma estrutura única

# Aprimorar

# Printar a soma de todos os valores pares digitados
# As somas dos valores da terceira coluna
# O maior valor da segunda linha

LISTA = []
DADOS = []
LINHA2 = []

SOMA3 = SOMA = 0

for perguntas in range(0 ,9):
    valor = (int(input('Digite um valor: ')))
    DADOS.append(valor)
    LISTA.append(DADOS[:])
    DADOS.clear()
    SOMA += valor
    if perguntas == 2 or perguntas == 5 or perguntas == 8:
        SOMA3 += valor
    if perguntas == 3 or perguntas == 4 or perguntas == 5:
        LINHA2.append(valor)

MAIOR = max(LINHA2)
    
print(f'''{LISTA[0]}   {LISTA[1]}   {LISTA[2]}
{LISTA[3]}   {LISTA[4]}   {LISTA[5]}
{LISTA[6]}   {LISTA[7]}   {LISTA[8]}''')

print('=' * 60)

print(f'A soma de todos os valores digitados vale: {SOMA}')
print(f'A soma dos valores da terceira coluna vale: {SOMA3}')
print(f'O maior valor da segunda linha vale: {MAIOR}')
