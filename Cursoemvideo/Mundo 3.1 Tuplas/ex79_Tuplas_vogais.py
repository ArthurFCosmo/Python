tupla = ('Amendoim', 'Guarana', 'Leite', 'Açucar', 'Vitamina', 'Gelo', 'Agua', 'Acai', 'Amazonas',
         'Doce', 'Gostoso', 'Crocante', 'Lanche')
for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end='')
