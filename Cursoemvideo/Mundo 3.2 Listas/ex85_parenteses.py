expressao = input('Digite a expressão: ')
pilha = list()
for laco in expressao:
    if laco == '(':
        pilha.append('(')
    elif laco ==(')'):
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
